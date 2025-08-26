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
    open(f"{cwd}/Data/CP/LeetCode/IO/_02017_GridGame_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_02017_GridGame_Output.txt", "w")


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(rft_stl.string_to_2D_list_of_int(input[i]))
        v0.append(int(input[i + 1]))


# endregion


# region Solutions
"""
Prefix and Suffix Sum
"""


def _02017_GridGame_0(grid: List[List[int]]) -> int:
    first_row_sum = sum(grid[0])
    second_row_sum = 0
    minimum_sum = float("inf")

    for turn_index in range(len(grid[0])):
        first_row_sum -= grid[0][turn_index]
        minimum_sum = min(minimum_sum, max(first_row_sum, second_row_sum))
        second_row_sum += grid[1][turn_index]

    return minimum_sum


def solve():
    for i in range(ncases):
        res0 = _02017_GridGame_0(v[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents 
the number of points at position (r, c) on the matrix. 
Two robots are playing a game on this matrix.
Both robots initially start at (0, 0) and want to reach (1, n-1). 
Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).
At the start of the game, the first robot moves from (0, 0) to (1, n-1), 
collecting all the points from the cells on its path. 
For all cells (r, c) traversed on the path, grid[r][c] is set to 0. 
Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. 
Note that their paths may intersect with one another.
The first robot wants to minimize the number of points collected by the second robot. 
In contrast, the second robot wants to maximize the number of points it collects. 
If both robots play optimally, return the number of points collected by the second robot.

Constraints:

grid.length == 2
n == grid[r].length
1 <= n <= 5 * 10^4
1 <= grid[r][c] <= 10^5
"""


def _02017_GridGame():
    os.system("cls")
    data_collector()
    solve()


_02017_GridGame()
# endregion


# region Unit Testing
class _02017_GridGame_Test(unittest.TestCase):
    def test_02017_GridGame_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02017_GridGame_0(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
