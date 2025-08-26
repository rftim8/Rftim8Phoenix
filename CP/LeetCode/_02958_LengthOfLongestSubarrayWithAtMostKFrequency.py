# region Imports
from collections import Counter
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
        f"{cwd}/Data/CP/LeetCode/IO/_02958_LengthOfLongestSubarrayWithAtMostKFrequency_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02958_LengthOfLongestSubarrayWithAtMostKFrequency_Output.txt",
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
        v.append(rft_stl.string_to_1D_list_of_int(input[i]))
        v0.append(int(input[i + 1]))
        v1.append(int(input[i + 2]))


# endregion


# region Solutions
"""
"""


def _02958_LengthOfLongestSubarrayWithAtMostKFrequency_0(
    nums: List[int], k: int
) -> int:
    res = 0
    l = -1
    f = Counter()
    for r in range(len(nums)):
        f[nums[r]] += 1
        while f[nums[r]] > k:
            l += 1
            f[nums[l]] -= 1
        res = max(res, r - l)

    return res


def solve():
    for i in range(ncases):
        res0 = _02958_LengthOfLongestSubarrayWithAtMostKFrequency_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
You are given an integer array nums and an integer k.
The frequency of an element x is the number of times it occurs in an array.
An array is called good if the frequency of each element in this array is less than or equal to k.
Return the length of the longest good subarray of nums.
A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= nums.length
"""


def _02958_LengthOfLongestSubarrayWithAtMostKFrequency():
    os.system("cls")
    data_collector()
    solve()


_02958_LengthOfLongestSubarrayWithAtMostKFrequency()
# endregion


# region Unit Testing
class _02958_LengthOfLongestSubarrayWithAtMostKFrequency_Test(unittest.TestCase):
    def test_02958_LengthOfLongestSubarrayWithAtMostKFrequency_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02958_LengthOfLongestSubarrayWithAtMostKFrequency_0(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
