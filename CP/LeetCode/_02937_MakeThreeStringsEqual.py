# region Imports
import os
from typing import List
import unittest
import sys

cwd = os.getcwd()
sys.path.append(cwd)
import rft_stl

# endregion


# region Data Gethering
input = (
    open(f"{cwd}/Data/CP/LeetCode/IO/_02937_MakeThreeStringsEqual_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_02937_MakeThreeStringsEqual_Output.txt", "w")


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []
v1 = []
v2 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(input[i])
        v0.append(input[i + 1])
        v1.append(input[i + 2])
        v2.append(int(input[i + 3]))


# endregion


# region Solutions
"""
"""


def _02937_MakeThreeStringsEqual_0(s1: str, s2: str, s3: str) -> int:
    m = len(s1) + len(s2) + len(s3)
    l = min(len(s1), len(s2), len(s3))
    c = 0
    for i in range(l):
        if s1[i] != s2[i] or s2[i] != s3[i]:
            return m - (c * 3) if c != 0 else -1
        else:
            c += 1

    return m - (l * 3)


def solve():
    for i in range(ncases):
        res0 = _02937_MakeThreeStringsEqual_0(v[i], v0[i], v1[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
You are given three strings: s1, s2, and s3. 
In one operation you can choose one of these strings and delete its rightmost character. 
Note that you cannot completely empty a string.
Return the minimum number of operations required to make the strings equal. 
If it is impossible to make them equal, return -1.

Constraints:

1 <= s1.length, s2.length, s3.length <= 100
s1, s2 and s3 consist only of lowercase English letters.
"""


def _02937_MakeThreeStringsEqual():
    os.system("cls")
    data_collector()
    solve()


_02937_MakeThreeStringsEqual()
# endregion


# region Unit Testing
class _02937_MakeThreeStringsEqual_Test(unittest.TestCase):
    def test_02937_MakeThreeStringsEqual_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02937_MakeThreeStringsEqual_0(v[i], v0[i], v1[i]),
                v2[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
