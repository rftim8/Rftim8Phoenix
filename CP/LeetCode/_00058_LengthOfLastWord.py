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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00058_LengthOfLastWord_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_00058_LengthOfLastWord_Output.txt", "w")


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(input[i])
        v0.append(int(input[i + 1]))


# endregion


# region Solutions
"""
"""


def _00058_LengthOfLastWord_0(s: str) -> int:
    res = 0
    c = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] != " ":
            c += 1
            res += 1
        else:
            if c > 0:
                break

    return res


"""
"""


def _00058_LengthOfLastWord_1(s: str) -> int:
    length = 0
    i = len(s) - 1
    while i >= 0 and s[i] == " ":
        i -= 1
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1
    return length


def solve():
    for i in range(ncases):
        res0 = _00058_LengthOfLastWord_0(v[i])
        output.writelines(str(res0) + "\n")
        res1 = _00058_LengthOfLastWord_1(v[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Constraints:

1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""


def _00058_LengthOfLastWord():
    os.system("cls")
    data_collector()
    solve()


_00058_LengthOfLastWord()
# endregion


# region Unit Testing
class _00058_LengthOfLastWord_Test(unittest.TestCase):
    def test_00058_LengthOfLastWord_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00058_LengthOfLastWord_0(v[i]),
                v0[i],
            )

    def test_00058_LengthOfLastWord_1(self):
        for i in range(ncases):
            self.assertEqual(
                _00058_LengthOfLastWord_1(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
