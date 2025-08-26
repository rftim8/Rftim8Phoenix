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
    open(f"{cwd}/Data/CP/LeetCode/IO/_02270_NumberOfWaysToSplitArray_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02270_NumberOfWaysToSplitArray_Output.txt", "w"
)


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(rft_stl.string_to_1D_list_of_int(input[i]))
        v0.append(int(input[i + 1]))


# endregion


# region Solutions
"""
Brute Force
"""


def _02270_NumberOfWaysToSplitArray_0(nums: List[int]) -> int:
    res = 0
    a = list(nums)
    b = list(nums)

    for i in range(1, len(a)):
        a[i] += a[i - 1]

    for i in range(len(b) - 2, -1, -1):
        b[i] += b[i + 1]

    for i in range(0, len(a) - 1):
        if a[i] >= b[i + 1]:
            res += 1

    return res


"""
Speed
"""


def _02270_NumberOfWaysToSplitArray_1(nums: List[int]) -> int:
    left = 0
    right = (sum(nums) + 1) // 2
    res = 0

    for i in range(len(nums) - 1):
        left += nums[i]
        if left >= right:
            res += 1

    return res


def solve():
    for i in range(ncases):
        res0 = _02270_NumberOfWaysToSplitArray_0(v[i])
        output.writelines(str(res0) + "\n")
        res1 = _02270_NumberOfWaysToSplitArray_1(v[i])
        output.writelines(str(res1) + "\n")


"""
Prefix Sum - Optimized
"""


def _02270_NumberOfWaysToSplitArray_2(nums: List[int]) -> int:
    halfSum = sum(nums) / 2
    left, res = 0, 0

    for n in nums[:-1]:
        left += n
        res += left >= halfSum

    return res


def solve():
    for i in range(ncases):
        res0 = _02270_NumberOfWaysToSplitArray_0(v[i])
        output.writelines(str(res0) + "\n")
        res1 = _02270_NumberOfWaysToSplitArray_1(v[i])
        output.writelines(str(res1) + "\n")
        res2 = _02270_NumberOfWaysToSplitArray_2(v[i])
        output.writelines(str(res2) + "\n")


# endregion


# region Problem Description
"""
You are given a 0-indexed integer array nums of length n.
nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.

Constraints:

2 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
"""


def _02270_NumberOfWaysToSplitArray():
    os.system("cls")
    data_collector()
    solve()


_02270_NumberOfWaysToSplitArray()
# endregion


# region Unit Testing
class _02270_NumberOfWaysToSplitArray_Test(unittest.TestCase):
    def test_02270_NumberOfWaysToSplitArray_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02270_NumberOfWaysToSplitArray_0(v[i]),
                v0[i],
            )

    def test_02270_NumberOfWaysToSplitArray_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02270_NumberOfWaysToSplitArray_1(v[i]),
                v0[i],
            )

    def test_02270_NumberOfWaysToSplitArray_2(self):
        for i in range(ncases):
            self.assertEqual(
                _02270_NumberOfWaysToSplitArray_2(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
