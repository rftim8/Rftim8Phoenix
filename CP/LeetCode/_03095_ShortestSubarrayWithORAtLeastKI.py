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
    open(f"{cwd}/Data/CP/LeetCode/IO/_03095_ShortestSubarrayWithORAtLeastKI_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_03095_ShortestSubarrayWithORAtLeastKI_Output.txt", "w"
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


def _03095_ShortestSubarrayWithORAtLeastKI_0(nums: List[int], k: int) -> int:
    res = 51
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            a = 0
            for l in range(i, j + 1):
                a |= nums[l]
            if a >= k:
                res = min(res, j - i + 1)

    return res if res != 51 else -1


def solve():
    for i in range(ncases):
        res0 = _03095_ShortestSubarrayWithORAtLeastKI_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
You are given an array nums of non-negative integers and an integer k.
An array is called special if the bitwise OR of all of its elements is at least k.
Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

Constraints:

1 <= nums.length <= 50
0 <= nums[i] <= 50
0 <= k < 64
"""


def _03095_ShortestSubarrayWithORAtLeastKI():
    os.system("cls")
    data_collector()
    solve()


_03095_ShortestSubarrayWithORAtLeastKI()
# endregion


# region Unit Testing
class _03095_ShortestSubarrayWithORAtLeastKI_Test(unittest.TestCase):
    def test_03095_ShortestSubarrayWithORAtLeastKI_0(self):
        for i in range(ncases):
            self.assertEqual(
                _03095_ShortestSubarrayWithORAtLeastKI_0(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
