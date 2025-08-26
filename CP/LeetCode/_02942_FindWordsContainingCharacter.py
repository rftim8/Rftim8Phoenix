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
    open(f"{cwd}/Data/CP/LeetCode/IO/_02942_FindWordsContainingCharacter_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02942_FindWordsContainingCharacter_Output.txt", "w"
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
        v1.append(rft_stl.string_to_1D_list_of_int(input[i + 2]))


# endregion


# region Solutions
"""
"""


def _02942_FindWordsContainingCharacter_0(words: List[str], x: str) -> List[int]:
    res = []
    for i, j in enumerate(words):
        if x in j:
            res.append(i)

    return res


def solve():
    for i in range(ncases):
        res0 = _02942_FindWordsContainingCharacter_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order.

Constraints:

1 <= words.length <= 50
1 <= words[i].length <= 50
x is a lowercase English letter.
words[i] consists only of lowercase English letters.
"""


def _02942_FindWordsContainingCharacter():
    os.system("cls")
    data_collector()
    solve()


_02942_FindWordsContainingCharacter()
# endregion


# region Unit Testing
class _02942_FindWordsContainingCharacter_Test(unittest.TestCase):
    def test_02942_FindWordsContainingCharacter_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02942_FindWordsContainingCharacter_0(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
