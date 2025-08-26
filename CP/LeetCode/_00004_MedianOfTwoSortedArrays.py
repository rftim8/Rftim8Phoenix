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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00004_MedianOfTwoSortedArrays_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_00004_MedianOfTwoSortedArrays_Output.txt", "w"
)


ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []
v1 = []


def data_collector():
    for i in range(2, ncases * nparams, nparams):
        v.append(rft_stl.string_to_1D_list_of_int(input[i]))
        v0.append(rft_stl.string_to_1D_list_of_int(input[i + 1]))
        v1.append(float(input[i + 2]))


# endregion


# region Solutions
"""
Math
"""


def _00004_MedianOfTwoSortedArrays_0(nums1: List[int], nums2: List[int]) -> float:
    l = len(nums1) + len(nums2)
    x = []
    for i in nums1:
        x.append(i)
    for i in nums2:
        x.append(i)
    x = sorted(x)

    return (
        float((x[int(l / 2) - 1] + x[int(l / 2)])) / 2
        if l % 2 == 0
        else float(x[int(l / 2)])
    )


"""
Binary Search
"""


def _00004_MedianOfTwoSortedArrays_1(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        return _00004_MedianOfTwoSortedArrays_1(nums2, nums1)

    m, n = len(nums1), len(nums2)
    left, right = 0, m

    while left <= right:
        partitionA = (left + right) // 2
        partitionB = (m + n + 1) // 2 - partitionA

        maxLeftA = float("-inf") if partitionA == 0 else nums1[partitionA - 1]
        minRightA = float("inf") if partitionA == m else nums1[partitionA]
        maxLeftB = float("-inf") if partitionB == 0 else nums2[partitionB - 1]
        minRightB = float("inf") if partitionB == n else nums2[partitionB]

        if maxLeftA <= minRightB and maxLeftB <= minRightA:
            if (m + n) % 2 == 0:
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
            else:
                return max(maxLeftA, maxLeftB)
        elif maxLeftA > minRightB:
            right = partitionA - 1
        else:
            left = partitionA + 1


def solve():
    for i in range(ncases):
        res0 = _00004_MedianOfTwoSortedArrays_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")
        res1 = _00004_MedianOfTwoSortedArrays_1(v[i], v0[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""


def _00004_MedianOfTwoSortedArrays():
    os.system("cls")
    data_collector()
    solve()


_00004_MedianOfTwoSortedArrays()
# endregion


# region Unit Testing
class _00004_MedianOfTwoSortedArrays_Test(unittest.TestCase):
    def test_00004_MedianOfTwoSortedArrays_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00004_MedianOfTwoSortedArrays_0(v[i], v0[i]),
                v1[i],
            )

    def test_00004_MedianOfTwoSortedArrays_1(self):
        for i in range(ncases):
            self.assertEqual(
                _00004_MedianOfTwoSortedArrays_1(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
