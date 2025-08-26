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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00916_WordSubsets_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_00916_WordSubsets_Output.txt", "w")


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []
v1 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(rft_stl.string_to_1D_list_of_string(input[i]))
        v0.append(rft_stl.string_to_1D_list_of_string(input[i + 1]))
        v1.append(rft_stl.string_to_1D_list_of_string(input[i + 2]))


# endregion


# region Solutions
"""
"""


def _00916_WordSubsets_0(words1: List[str], words2: List[str]) -> List[str]:
    def count(word):
        res = [0] * 26
        for letter in word:
            res[ord(letter) - ord("a")] += 1
        return res

    bmax = [0] * 26
    for b in words2:
        for i, c in enumerate(count(b)):
            bmax[i] = max(bmax[i], c)

    res = []
    for a in words1:
        if all(x >= y for x, y in zip(count(a), bmax)):
            res.append(a)
    return res


"""
"""


def _00916_WordSubsets_1(words1: List[str], words2: List[str]) -> List[str]:
    res = set(words1)
    letters = {}
    for i in words2:
        for j in i:
            count = i.count(j)
            if j not in letters or count > letters[j]:
                letters[j] = count
    for i in words1:
        for j in letters:
            if i.count(j) < letters[j]:
                res.remove(i)
                break
    return list(res)


def solve():
    for i in range(ncases):
        res0 = sorted(_00916_WordSubsets_0(v[i], v0[i]))
        output.writelines(str(res0) + "\n")

        res1 = sorted(_00916_WordSubsets_1(v[i], v0[i]))
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
You are given two string arrays words1 and words2.
A string b is a subset of string a if every letter in b occurs in a including multiplicity.
For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.
Return an array of all the universal strings in words1. You may return the answer in any order.

Constraints:

1 <= words1.length, words2.length <= 10^4
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
"""


def _00916_WordSubsets():
    os.system("cls")
    data_collector()
    solve()


_00916_WordSubsets()
# endregion


# region Unit Testing
class _00916_WordSubsets_Test(unittest.TestCase):
    def test_00916_WordSubsets_0(self):
        for i in range(ncases):
            actual = sorted(_00916_WordSubsets_0(v[i], v0[i]))
            expected = sorted(v1[i])
            self.assertEqual(
                actual,
                expected,
            )

    def test_00916_WordSubsets_1(self):
        for i in range(ncases):
            actual = sorted(_00916_WordSubsets_1(v[i], v0[i]))
            expected = sorted(v1[i])
            self.assertEqual(
                actual,
                expected,
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
