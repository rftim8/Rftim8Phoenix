# region Imports
from collections import defaultdict
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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00992_SubarraysWithKDifferentIntegers_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_00992_SubarraysWithKDifferentIntegers_Output.txt", "w"
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
Sliding Window
"""


def _00992_SubarraysWithKDifferentIntegers_0(nums: List[int], k: int) -> int:
    dist = defaultdict(int)

    res = 0
    l = 0
    r = 0
    c = 0

    while r < len(nums):
        dist[nums[r]] += 1

        if dist[nums[r]] == 1:
            k -= 1

        if k < 0:
            dist[nums[l]] -= 1
            if dist[nums[l]] == 0:
                k += 1
            l += 1
            c = 0

        if k == 0:
            while dist[nums[l]] > 1:
                dist[nums[l]] -= 1
                l += 1
                c += 1
            res += c + 1

        r += 1

    return res


"""
Speed
"""


def _00992_SubarraysWithKDifferentIntegers_1(nums: List[int], k: int) -> int:
    def f(counts=[0] * (len(nums) + 1), low=0, high=0, k=k):
        for num in nums:
            if not counts[num]:
                if (k := k - 1) < 0:
                    counts[nums[high]] = 0
                    low = high = high + 1
            counts[num] += 1
            if k <= 0:
                while counts[(a := nums[high])] > 1:
                    counts[a] -= 1
                    high += 1
                yield high - low + 1

    return sum(f())


"""
Greedy
"""


def _00992_SubarraysWithKDifferentIntegers_2(nums: List[int], k: int) -> int:
    res = 0

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if len(set(nums[i : j + 1])) == k:
                res += 1

    return res


def solve():
    for i in range(ncases):
        res0 = _00992_SubarraysWithKDifferentIntegers_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")

        res1 = _00992_SubarraysWithKDifferentIntegers_1(v[i], v0[i])
        output.writelines(str(res1) + "\n")

        res2 = _00992_SubarraysWithKDifferentIntegers_2(v[i], v0[i])
        output.writelines(str(res2) + "\n")


# endregion


# region Problem Description
"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Constraints:

1 <= nums.length <= 2 * 10^4
1 <= nums[i], k <= nums.length
"""


def _00992_SubarraysWithKDifferentIntegers():
    os.system("cls")
    data_collector()
    solve()


_00992_SubarraysWithKDifferentIntegers()
# endregion


# region Unit Testing
class _00992_SubarraysWithKDifferentIntegers_Test(unittest.TestCase):
    def test_00992_SubarraysWithKDifferentIntegers_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00992_SubarraysWithKDifferentIntegers_0(v[i], v0[i]),
                v1[i],
            )

    def test_00992_SubarraysWithKDifferentIntegers_1(self):
        for i in range(ncases):
            self.assertEqual(
                _00992_SubarraysWithKDifferentIntegers_1(v[i], v0[i]),
                v1[i],
            )

    def test_00992_SubarraysWithKDifferentIntegers_2(self):
        for i in range(ncases):
            self.assertEqual(
                _00992_SubarraysWithKDifferentIntegers_2(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
