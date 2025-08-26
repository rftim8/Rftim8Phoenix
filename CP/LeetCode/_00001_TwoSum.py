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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00001_TwoSum_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_00001_TwoSum_Output.txt", "w")


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
        v1.append(rft_stl.string_to_1D_list_of_int(input[i + 2]))


# endregion


# region Solutions
"""
Brute Force
Time: O(n^2)
Space: O(1)
"""


def _00001_TwoSum_0(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


"""
Two-Pass Hash Table
Time: O(n), dictionary reduces lookup time
Space: O(1)
"""


def _00001_TwoSum_1(nums: List[int], target: int) -> List[int]:
    dict = {}

    for i in range(len(nums)):
        dict[nums[i]] = i

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dict and dict[complement] != i:
            return [i, dict[complement]]

    return []


"""
One-Pass Hash Table
Time: O(n), dictionary reduces lookup time
Space: O(1)
"""


def _00001_TwoSum_2(nums: List[int], target: int) -> List[int]:
    dict = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dict:
            return [dict[complement], i]
        dict[nums[i]] = i

    return []


def solve():
    for i in range(ncases):
        res0 = _00001_TwoSum_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")
        res1 = _00001_TwoSum_1(v[i], v0[i])
        output.writelines(str(res1) + "\n")
        res2 = _00001_TwoSum_2(v[i], v0[i])
        output.writelines(str(res2) + "\n")


# endregion


# region Problem Description
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
"""


def _00001_TwoSum():
    os.system("cls")
    data_collector()
    solve()


_00001_TwoSum()
# endregion


# region Unit Testing
class _00001_TwoSum_Test(unittest.TestCase):
    def test_00001_TwoSum_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00001_TwoSum_0(v[i], v0[i]),
                v1[i],
            )

    def test_00001_TwoSum_1(self):
        for i in range(ncases):
            self.assertEqual(
                _00001_TwoSum_1(v[i], v0[i]),
                v1[i],
            )

    def test_00001_TwoSum_2(self):
        for i in range(ncases):
            self.assertEqual(
                _00001_TwoSum_2(v[i], v0[i]),
                v1[i],
            )


# unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
