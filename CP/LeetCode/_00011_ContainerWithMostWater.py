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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00011_ContainerWithMostWater_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_00011_ContainerWithMostWater_Output.txt", "w"
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
Brute Force - TLE
"""


def _00011_ContainerWithMostWater_0(height: List[int]) -> int:
    res = 0
    l = len(height)
    for i in range(l):
        for j in range(i + 1, l):
            h = min(height[i], height[j])
            w = j - i
            res = max(res, w * h)
    return res


"""
Two Pointers
"""


def _00011_ContainerWithMostWater_1(height: List[int]) -> int:
    n = len(height)
    res = 0
    l = 0
    r = n - 1
    while l < r:
        h = min(height[l], height[r])
        w = r - l
        res = max(res, h * w)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res


"""
Speed
"""


def _00011_ContainerWithMostWater_2(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    ans = 0
    while l < r:
        ans = max(ans, abs(l - r) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return ans


def solve():
    for i in range(ncases):
        res0 = _00011_ContainerWithMostWater_0(v[i])
        output.writelines(str(res0) + "\n")
        res1 = _00011_ContainerWithMostWater_1(v[i])
        output.writelines(str(res1) + "\n")
        res2 = _00011_ContainerWithMostWater_2(v[i])
        output.writelines(str(res2) + "\n")


# endregion


# region Problem Description
"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""


def _00011_ContainerWithMostWater():
    os.system("cls")
    data_collector()
    solve()


_00011_ContainerWithMostWater()
# endregion


# region Unit Testing
class _00011_ContainerWithMostWater_Test(unittest.TestCase):
    def test_00011_ContainerWithMostWater_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00011_ContainerWithMostWater_0(v[i]),
                v0[i],
            )

    def test_00011_ContainerWithMostWater_1(self):
        for i in range(ncases):
            self.assertEqual(
                _00011_ContainerWithMostWater_1(v[i]),
                v0[i],
            )

    def test_00011_ContainerWithMostWater_2(self):
        for i in range(ncases):
            self.assertEqual(
                _00011_ContainerWithMostWater_2(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
