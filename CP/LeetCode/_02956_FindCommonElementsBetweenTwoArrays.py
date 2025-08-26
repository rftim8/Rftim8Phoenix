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
    open(
        f"{cwd}/Data/CP/LeetCode/IO/_02956_FindCommonElementsBetweenTwoArrays_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02956_FindCommonElementsBetweenTwoArrays_Output.txt",
    "w",
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
        v0.append(rft_stl.string_to_1D_list_of_int(input[i + 1]))
        v1.append(rft_stl.string_to_1D_list_of_int(input[i + 2]))


# endregion


# region Solutions
"""
"""


def _02956_FindCommonElementsBetweenTwoArrays_0(
    nums1: List[int], nums2: List[int]
) -> List[int]:
    res = []
    a0 = {}
    b0 = {}

    for i in nums1:
        if i in a0:
            a0[i] += 1
        else:
            a0[i] = 1
    for i in nums2:
        if i in b0:
            b0[i] += 1
        else:
            b0[i] = 1
    c = 0
    for i in a0:
        if i in b0:
            c += a0[i]
    res.append(c)
    c = 0
    for i in b0:
        if i in a0:
            c += b0[i]
    res.append(c)

    return res


"""
"""


def _02956_FindCommonElementsBetweenTwoArrays_1(
    nums1: List[int], nums2: List[int]
) -> List[int]:
    s1 = set(nums1)
    s2 = set(nums2)
    c1 = 0
    c2 = 0

    for n in nums1:
        if n in s2:
            c1 += 1

    for n in nums2:
        if n in s1:
            c2 += 1

    return [c1, c2]


def solve():
    for i in range(ncases):
        res0 = _02956_FindCommonElementsBetweenTwoArrays_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")

        res1 = _02956_FindCommonElementsBetweenTwoArrays_1(v[i], v0[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. 
Calculate the following values:
answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2].

Constraints:

n == nums1.length
m == nums2.length
1 <= n, m <= 100
1 <= nums1[i], nums2[i] <= 100
"""


def _02956_FindCommonElementsBetweenTwoArrays():
    os.system("cls")
    data_collector()
    solve()


_02956_FindCommonElementsBetweenTwoArrays()
# endregion


# region Unit Testing
class _02956_FindCommonElementsBetweenTwoArrays_Test(unittest.TestCase):
    def test_02956_FindCommonElementsBetweenTwoArrays_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02956_FindCommonElementsBetweenTwoArrays_0(v[i], v0[i]),
                v1[i],
            )

    def test_02956_FindCommonElementsBetweenTwoArrays_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02956_FindCommonElementsBetweenTwoArrays_1(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
