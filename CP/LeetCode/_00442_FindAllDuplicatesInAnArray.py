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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00442_FindAllDuplicatesInAnArray_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_00442_FindAllDuplicatesInAnArray_Output.txt", "w"
)


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(rft_stl.string_to_1D_list_of_int(input[i]))
        v0.append(rft_stl.string_to_1D_list_of_int(input[i + 1]))


# endregion


# region Solutions
"""
"""


def _00442_FindAllDuplicatesInAnArray_0(nums: List[int]) -> List[int]:
    res = []
    kvp = {}
    for i in nums:
        if not i in kvp:
            kvp[i] = 1
        else:
            res.append(i)

    return res


"""
"""


def _00442_FindAllDuplicatesInAnArray_1(nums: List[int]) -> List[int]:
    duplicatemap = {}
    for i in nums:
        if i in duplicatemap:
            duplicatemap[i] += 1
        else:
            duplicatemap[i] = 1

    return sorted([k for k, v in duplicatemap.items() if v >= 2])


def solve():
    for i in range(ncases):
        res0 = _00442_FindAllDuplicatesInAnArray_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _00442_FindAllDuplicatesInAnArray_1(v[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and 
each integer appears at most twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, 
excluding the space needed to store the output

Constraints:

n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""


def _00442_FindAllDuplicatesInAnArray():
    os.system("cls")
    data_collector()
    solve()


_00442_FindAllDuplicatesInAnArray()
# endregion


# region Unit Testing
class _00442_FindAllDuplicatesInAnArray_Test(unittest.TestCase):
    def test_00442_FindAllDuplicatesInAnArray_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00442_FindAllDuplicatesInAnArray_0(v[i]),
                v0[i],
            )

    def test_00442_FindAllDuplicatesInAnArray_1(self):
        for i in range(ncases):
            self.assertEqual(
                _00442_FindAllDuplicatesInAnArray_1(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
