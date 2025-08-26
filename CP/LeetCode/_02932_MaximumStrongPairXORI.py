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
    open(f"{cwd}/Data/CP/LeetCode/IO/_02932_MaximumStrongPairXORI_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_02932_MaximumStrongPairXORI_Output.txt", "w")


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
"""


def _02932_MaximumStrongPairXORI_0(nums: List[int]) -> int:
    res = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                res = max(res, nums[i] ^ nums[j])
    return res


def solve():
    for i in range(ncases):
        res0 = _02932_MaximumStrongPairXORI_0(v[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
You are given a 0-indexed integer array nums. 
A pair of integers x and y is called a strong pair if it satisfies the condition:
|x - y| <= min(x, y)
You need to select two integers from nums such that they form a strong pair and their bitwise XOR 
is the maximum among all strong pairs in the array.
Return the maximum XOR value out of all possible strong pairs in the array nums.
Note that you can pick the same integer twice to form a pair.

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 100
"""


def _02932_MaximumStrongPairXORI():
    os.system("cls")
    data_collector()
    solve()


_02932_MaximumStrongPairXORI()
# endregion


# region Unit Testing
class _02932_MaximumStrongPairXORI_Test(unittest.TestCase):
    def test_02932_MaximumStrongPairXORI_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02932_MaximumStrongPairXORI_0(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
