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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00713_SubarrayProductLessThanK_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_00713_SubarrayProductLessThanK_Output.txt", "w"
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


def _00713_SubarrayProductLessThanK_0(nums: List[int], k: int) -> int:
    res = 0
    if k <= 1:
        return res

    l = 0
    mid = 1

    for i in range(0, len(nums)):
        mid *= nums[i]
        while mid >= k:
            mid /= nums[l]
            l += 1
        res += i - l + 1

    return res


def solve():
    for i in range(ncases):
        res0 = _00713_SubarrayProductLessThanK_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where 
the product of all the elements in the subarray is strictly less than k.

Constraints:

1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6
"""


def _00713_SubarrayProductLessThanK():
    os.system("cls")
    data_collector()
    solve()


_00713_SubarrayProductLessThanK()
# endregion


# region Unit Testing
class _00713_SubarrayProductLessThanK_Test(unittest.TestCase):
    def test_00713_SubarrayProductLessThanK_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00713_SubarrayProductLessThanK_0(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
