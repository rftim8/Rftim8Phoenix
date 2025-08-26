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
    open(
        f"{cwd}/Data/CP/LeetCode/IO/_02900_LongestUnequalAdjacentGroupsSubsequenceI_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02900_LongestUnequalAdjacentGroupsSubsequenceI_Output.txt",
    "w",
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
        v0.append(rft_stl.string_to_1D_list_of_int(input[i + 1]))
        v1.append(rft_stl.string_to_1D_list_of_string(input[i + 2]))


# endregion


# region Solutions
"""
"""


def _02900_LongestUnequalAdjacentGroupsSubsequenceI_0(
    words: List[str], groups: List[int]
) -> List[str]:
    b0 = False
    b1 = False
    l = []
    for i in range(len(groups)):
        if b0 == True and b1 == True:
            break
        b = groups[i]
        if b == 0:
            b0 = True
        if b == 1:
            b1 = True
        t = [words[i]]
        for j in range(i + 1, len(groups)):
            if groups[j] != b:
                t.append(words[j])
                b = groups[j]
        l.append(t)

    return max(l, key=lambda o: len(o))


def solve():
    for i in range(ncases):
        res0 = _02900_LongestUnequalAdjacentGroupsSubsequenceI_0(v[i], v0[i])
        output.writelines(j + " " for j in res0)
        output.write("\n")


# endregion


# region Problem Description
"""
You are given a string array words and a binary array groups both of length n, 
where words[i] is associated with groups[i].
Your task is to select the longest alternating subsequence from words.
A subsequence of words is alternating if for any two consecutive strings in the sequence, 
their corresponding elements in the binary array groups differ. 
Essentially, you are to choose strings such that adjacent elements have non-matching corresponding bits 
in the groups array.
Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1] denoted as 
[i0, i1, ..., ik-1], such that groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and then 
find the words corresponding to these indices.
Return the selected subsequence. 
If there are multiple answers, return any of them.
Note: The elements in words are distinct.

Constraints:

1 <= n == words.length == groups.length <= 100
1 <= words[i].length <= 10
groups[i] is either 0 or 1.
words consists of distinct strings.
words[i] consists of lowercase English letters.
"""


def _02900_LongestUnequalAdjacentGroupsSubsequenceI():
    os.system("cls")
    data_collector()
    solve()


_02900_LongestUnequalAdjacentGroupsSubsequenceI()
# endregion


# region Unit Testing
class _02900_LongestUnequalAdjacentGroupsSubsequenceI_Test(unittest.TestCase):
    def test_02900_LongestUnequalAdjacentGroupsSubsequenceI_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02900_LongestUnequalAdjacentGroupsSubsequenceI_0(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
