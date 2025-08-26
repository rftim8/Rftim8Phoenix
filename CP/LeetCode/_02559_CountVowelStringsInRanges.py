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
    open(f"{cwd}/Data/CP/LeetCode/IO/_02559_CountVowelStringsInRanges_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02559_CountVowelStringsInRanges_Output.txt", "w"
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
        v0.append(rft_stl.string_to_2D_list_of_int(input[i + 1]))
        v1.append(rft_stl.string_to_1D_list_of_int(input[i + 2]))


# endregion


# region Solutions
"""
"""


def _02559_CountVowelStringsInRanges_0(
    words: List[str], queries: List[List[int]]
) -> List[int]:
    ans = [0] * len(queries)
    vowels = {"a", "e", "i", "o", "u"}
    prefix_sum = [0] * len(words)
    sum = 0

    for i in range(len(words)):
        current_word = words[i]
        if current_word[0] in vowels and current_word[len(current_word) - 1] in vowels:
            sum += 1
        prefix_sum[i] = sum

    for i in range(len(queries)):
        current_query = queries[i]
        ans[i] = prefix_sum[current_query[1]] - (
            0 if current_query[0] == 0 else prefix_sum[current_query[0] - 1]
        )

    return ans


"""
"""


def _02559_CountVowelStringsInRanges_1(
    words: List[str], queries: List[List[int]]
) -> List[int]:
    prefix = [0]
    cur = 0
    vowelSet = set(["a", "e", "i", "o", "u"])

    for s in words:
        if s[0] in vowelSet and s[-1] in vowelSet:
            cur += 1

        prefix.append(cur)

    res = []

    for s, e in queries:
        res.append(prefix[e + 1] - prefix[s])

    return res


def solve():
    for i in range(ncases):
        res0 = _02559_CountVowelStringsInRanges_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")
        res1 = _02559_CountVowelStringsInRanges_1(v[i], v0[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
You are given a 0-indexed array of strings words and a 2D array of integers queries.
Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri
(both inclusive) of words that start and end with a vowel.
Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

Constraints:

1 <= words.length <= 10^5
1 <= words[i].length <= 40
words[i] consists only of lowercase English letters.
sum(words[i].length) <= 3 * 10^5
1 <= queries.length <= 10^5
0 <= li <= ri < words.length
"""


def _02559_CountVowelStringsInRanges():
    os.system("cls")
    data_collector()
    solve()


_02559_CountVowelStringsInRanges()
# endregion


# region Unit Testing
class _02559_CountVowelStringsInRanges_Test(unittest.TestCase):
    def test_02559_CountVowelStringsInRanges_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02559_CountVowelStringsInRanges_0(v[i], v0[i]),
                v1[i],
            )

    def test_02559_CountVowelStringsInRanges_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02559_CountVowelStringsInRanges_1(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
