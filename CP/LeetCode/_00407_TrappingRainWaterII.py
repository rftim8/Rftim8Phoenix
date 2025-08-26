# region Imports
import copy
import heapq
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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00407_TrappingRainWaterII_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_00407_TrappingRainWaterII_Output.txt", "w")


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
BFS + Priority Queue
"""


class Cell:
    def __init__(self, height, row, col):
        self.height = height
        self.row = row
        self.col = col

    def __lt__(self, other):
        return self.height < other.height


def _is_valid_cell(row, col, num_of_rows, num_of_cols):
    return 0 <= row < num_of_rows and 0 <= col < num_of_cols


def _00407_TrappingRainWaterII_0(heightMap0: List[List[int]]) -> int:
    heightMap = copy.deepcopy(heightMap0)
    d_row = [0, 0, -1, 1]
    d_col = [-1, 1, 0, 0]
    num_of_rows = len(heightMap)
    num_of_cols = len(heightMap[0])
    visited = [[False] * num_of_cols for _ in range(num_of_rows)]
    boundary = []

    for i in range(num_of_rows):
        heapq.heappush(boundary, Cell(heightMap[i][0], i, 0))
        heapq.heappush(
            boundary,
            Cell(heightMap[i][num_of_cols - 1], i, num_of_cols - 1),
        )
        visited[i][0] = visited[i][num_of_cols - 1] = True

    for i in range(num_of_cols):
        heapq.heappush(boundary, Cell(heightMap[0][i], 0, i))
        heapq.heappush(
            boundary,
            Cell(heightMap[num_of_rows - 1][i], num_of_rows - 1, i),
        )
        visited[0][i] = visited[num_of_rows - 1][i] = True

    total_water_volume = 0

    while boundary:
        current_cell = heapq.heappop(boundary)
        current_row = current_cell.row
        current_col = current_cell.col
        min_boundary_height = current_cell.height

        for direction in range(4):
            neighbor_row = current_row + d_row[direction]
            neighbor_col = current_col + d_col[direction]

            if (
                _is_valid_cell(neighbor_row, neighbor_col, num_of_rows, num_of_cols)
                and not visited[neighbor_row][neighbor_col]
            ):
                neighbor_height = heightMap[neighbor_row][neighbor_col]

                if neighbor_height < min_boundary_height:
                    total_water_volume += min_boundary_height - neighbor_height

                heapq.heappush(
                    boundary,
                    Cell(
                        max(neighbor_height, min_boundary_height),
                        neighbor_row,
                        neighbor_col,
                    ),
                )
                visited[neighbor_row][neighbor_col] = True

    return total_water_volume


"""
Speed
"""


def _00407_TrappingRainWaterII_1(heightMap0: List[List[int]]) -> int:
    heightMap = copy.deepcopy(heightMap0)
    M = len(heightMap)
    N = len(heightMap[0])
    h = []

    for i in [0, M - 1]:
        for j in range(N):
            h.append((heightMap[i][j], i, j))
            heightMap[i][j] = -1

    for i in range(1, M - 1):
        for j in [0, N - 1]:
            h.append((heightMap[i][j], i, j))
            heightMap[i][j] = -1

    heapq.heapify(h)

    tot = 0
    while h:
        height, x, y = heapq.heappop(h)
        stack = [(x, y)]
        while h and h[0][0] == height:
            _, x, y = heapq.heappop(h)
            stack.append((x, y))
        while stack:
            x, y = stack.pop()
            for d in [-1, 1]:
                nX = x + d
                nY = y + d
                if 0 > nX or M <= nX or heightMap[nX][y] == -1:
                    pass
                else:
                    if height > heightMap[nX][y]:
                        tot += height - heightMap[nX][y]
                        stack.append((nX, y))
                        heightMap[nX][y] = -1
                    else:
                        heapq.heappush(h, (heightMap[nX][y], nX, y))
                        heightMap[nX][y] = -1

                if 0 > nY or N <= nY or heightMap[x][nY] == -1:
                    pass
                else:
                    if height > heightMap[x][nY]:
                        tot += height - heightMap[x][nY]
                        stack.append((x, nY))
                        heightMap[x][nY] = -1
                    else:
                        heapq.heappush(h, (heightMap[x][nY], x, nY))
                        heightMap[x][nY] = -1

    return tot


def solve():
    for i in range(ncases):
        res0 = _00407_TrappingRainWaterII_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _00407_TrappingRainWaterII_1(v[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
Given an m x n integer matrix heightMap representing the height of each unit cell 
in a 2D elevation map, return the volume of water it can trap after raining.
Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 10^4
"""


def _00407_TrappingRainWaterII():
    os.system("cls")
    data_collector()
    solve()


_00407_TrappingRainWaterII()
# endregion


# region Unit Testing
class _00407_TrappingRainWaterII_Test(unittest.TestCase):
    def test_00407_TrappingRainWaterII_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00407_TrappingRainWaterII_0(v[i]),
                v0[i],
            )

    def test_00407_TrappingRainWaterII_1(self):
        for i in range(ncases):
            self.assertEqual(
                _00407_TrappingRainWaterII_1(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
