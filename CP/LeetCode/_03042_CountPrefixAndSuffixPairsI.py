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
    open(f"{cwd}/Data/CP/LeetCode/IO/_03042_CountPrefixAndSuffixPairsI_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_03042_CountPrefixAndSuffixPairsI_Output.txt", "w"
)


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(rft_stl.string_to_1D_list_of_string(input[i]))
        v0.append(int(input[i + 1]))


# endregion


# region Solutions
"""
"""


def _03042_CountPrefixAndSuffixPairsI_0(words: List[str]) -> int:
    res = 0

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                res += 1

    return res


def solve():
    for i in range(ncases):
        res0 = _03042_CountPrefixAndSuffixPairsI_0(v[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
You are given a 0-indexed string array words.
Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, 
and false otherwise.
For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, 
but isPrefixAndSuffix("abc", "abcd") is false.
Return an integer denoting the number of index pairs (i, j) such that i < j, and 
isPrefixAndSuffix(words[i], words[j]) is true.

Constraints:

1 <= words.length <= 50
1 <= words[i].length <= 10
words[i] consists only of lowercase English letters.
"""


def _03042_CountPrefixAndSuffixPairsI():
    os.system("cls")
    data_collector()
    solve()


_03042_CountPrefixAndSuffixPairsI()
# endregion


# region Unit Testing
class _03042_CountPrefixAndSuffixPairsI_Test(unittest.TestCase):
    def test_03042_CountPrefixAndSuffixPairsI_0(self):
        for i in range(ncases):
            self.assertEqual(
                _03042_CountPrefixAndSuffixPairsI_0(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
