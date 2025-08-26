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
    open(f"{cwd}/Data/CP/LeetCode/IO/_02185_CountingWordsWithAGivenPrefix_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02185_CountingWordsWithAGivenPrefix_Output.txt", "w"
)


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []
v1 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(rft_stl.string_to_1D_list_of_string(input[i]))
        v0.append(input[i + 1])
        v1.append(int(input[i + 2]))


# endregion


# region Solutions
"""
"""


def _02185_CountingWordsWithAGivenPrefix_0(words: List[str], pref: str) -> int:
    res = 0

    for i in words:
        if i.startswith(pref):
            res += 1

    return res


def solve():
    for i in range(ncases):
        res0 = _02185_CountingWordsWithAGivenPrefix_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s.

Constraints:

1 <= words.length <= 100
1 <= words[i].length, pref.length <= 100
words[i] and pref consist of lowercase English letters.
"""


def _02185_CountingWordsWithAGivenPrefix():
    os.system("cls")
    data_collector()
    solve()


_02185_CountingWordsWithAGivenPrefix()
# endregion


# region Unit Testing
class _02185_CountingWordsWithAGivenPrefix_Test(unittest.TestCase):
    def test_02185_CountingWordsWithAGivenPrefix_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02185_CountingWordsWithAGivenPrefix_0(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
