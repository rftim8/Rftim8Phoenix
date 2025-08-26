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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00205_IsomorphicStrings_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_00205_IsomorphicStrings_Output.txt", "w")


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []
v1 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(input[i])
        v0.append(input[i + 1])
        v1.append(True if input[i + 2] == "true" else False)


# endregion


# region Solutions
"""
"""


def _00205_IsomorphicStrings_0(s: str, t: str) -> bool:
    d = {}
    for i in range(len(t)):
        if not t[i] in d:
            d[t[i]] = s[i]
        else:
            if d[t[i]] != s[i]:
                return False

    e = {}
    for i in range(len(s)):
        if not s[i] in e:
            e[s[i]] = t[i]
        else:
            if e[s[i]] != t[i]:
                return False

    return True


def solve():
    for i in range(ncases):
        res0 = _00205_IsomorphicStrings_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Constraints:

1 <= s.length <= 5 * 10^4
t.length == s.length
s and t consist of any valid ascii character.
"""


def _00205_IsomorphicStrings():
    os.system("cls")
    data_collector()
    solve()


_00205_IsomorphicStrings()
# endregion


# region Unit Testing
class _00205_IsomorphicStrings_Test(unittest.TestCase):
    def test_00205_IsomorphicStrings_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00205_IsomorphicStrings_0(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
