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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00015_ThreeSum_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_00015_ThreeSum_Output.txt", "w")


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(rft_stl.string_to_1D_list_of_int(input[i]))
        v0.append(rft_stl.string_to_2D_list_of_int(input[i + 1]))


# endregion


# region Solutions
"""
Greedy
"""


def _00015_ThreeSum_0(nums: List[int]) -> List[List[int]]:
    res = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    b = sorted([nums[i], nums[j], nums[k]])
                    if not b in res:
                        res.append(b)

    return res


"""
Two Pointers
"""


def _00015_ThreeSum_1(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i, b in enumerate(nums):
        if i > 0 and b == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while r > l:
            k = b + nums[l] + nums[r]
            if k > 0:
                r -= 1
            elif k < 0:
                l += 1
            else:
                res.append([b, nums[r], nums[l]])
                l += 1
                while nums[l] == nums[l - 1] and r > l:
                    l += 1

    return res


def solve():
    for i in range(ncases):
        res0 = sorted(sorted(i) for i in _00015_ThreeSum_0(v[i]))
        output.writelines(str(res0) + "\n")
        res1 = sorted(sorted(i) for i in _00015_ThreeSum_1(v[i]))
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Constraints:

3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""


def _00015_ThreeSum():
    os.system("cls")
    data_collector()
    solve()


_00015_ThreeSum()
# endregion


# region Unit Testing
class _00015_ThreeSum_Test(unittest.TestCase):
    def test_00015_ThreeSum_0(self):
        for i in range(ncases):
            actual = sorted(sorted(i) for i in _00015_ThreeSum_0(v[i]))
            expected = sorted(sorted(i) for i in v0[i])
            self.assertEqual(
                actual,
                expected,
            )

    def test_00015_ThreeSum_1(self):
        for i in range(ncases):
            actual = sorted(sorted(i) for i in _00015_ThreeSum_1(v[i]))
            expected = sorted(sorted(i) for i in v0[i])
            self.assertEqual(
                actual,
                expected,
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
