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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00041_FirstMissingPositive_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_00041_FirstMissingPositive_Output.txt", "w")


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


def _00041_FirstMissingPositive_0(nums: List[int]) -> int:
    b = {}
    c = 0
    for i in nums:
        if i > 0:
            b[i] = 1
            c = max(c, i)
    for i in range(1, c):
        if not i in b:
            return i
    return c + 1


"""
"""


def _00041_FirstMissingPositive_1(nums: List[int]) -> int:
    b = set(map(int, nums))
    res = 1
    while res in b:
        res += 1

    return res


def solve():
    for i in range(ncases):
        res0 = _00041_FirstMissingPositive_0(v[i])
        output.writelines(str(res0) + "\n")
        res1 = _00041_FirstMissingPositive_1(v[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Constraints:

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""


def _00041_FirstMissingPositive():
    os.system("cls")
    data_collector()
    solve()


_00041_FirstMissingPositive()
# endregion


# region Unit Testing
class _00041_FirstMissingPositive_Test(unittest.TestCase):
    def test_00041_FirstMissingPositive_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00041_FirstMissingPositive_0(v[i]),
                v0[i],
            )

    def test_00041_FirstMissingPositive_1(self):
        for i in range(ncases):
            self.assertEqual(
                _00041_FirstMissingPositive_1(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
