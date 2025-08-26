# region Imports
from collections import deque
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
    open(f"{cwd}/Data/CP/LeetCode/IO/_01765_MapOfHighestPeak_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_01765_MapOfHighestPeak_Output.txt", "w")


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(rft_stl.string_to_2D_list_of_int(input[i]))
        v0.append(rft_stl.string_to_2D_list_of_int(input[i + 1]))


# endregion


# region Solutions
"""
BFS
"""


def _is_valid_cell(x, y, rows, columns):
    return 0 <= x < rows and 0 <= y < columns


def _01765_MapOfHighestPeak_0(isWater: List[List[int]]) -> List[List[int]]:
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows = len(isWater)
    columns = len(isWater[0])
    cell_heights = [[-1 for _ in range(columns)] for _ in range(rows)]
    cell_queue = deque()

    for x in range(rows):
        for y in range(columns):
            if isWater[x][y] == 1:
                cell_queue.append((x, y))
                cell_heights[x][y] = 0

    height_of_next_layer = 1

    while cell_queue:
        layer_size = len(cell_queue)

        for _ in range(layer_size):
            current_cell = cell_queue.popleft()

            for d in range(4):
                neighbor_x = current_cell[0] + dx[d]
                neighbor_y = current_cell[1] + dy[d]

                if (
                    _is_valid_cell(neighbor_x, neighbor_y, rows, columns)
                    and cell_heights[neighbor_x][neighbor_y] == -1
                ):
                    cell_heights[neighbor_x][neighbor_y] = height_of_next_layer
                    cell_queue.append((neighbor_x, neighbor_y))

        height_of_next_layer += 1

    return cell_heights


"""
DP
"""


def _01765_MapOfHighestPeak_1(isWater: List[List[int]]) -> List[List[int]]:
    rows = len(isWater)
    columns = len(isWater[0])
    INF = rows * columns
    cell_heights = [[INF] * columns for _ in range(rows)]

    for row in range(rows):
        for col in range(columns):
            if isWater[row][col] == 1:
                cell_heights[row][col] = 0

    for row in range(rows):
        for col in range(columns):
            min_neighbor_distance = INF
            neighbor_row = row - 1
            neighbor_col = col
            if _is_valid_cell(neighbor_row, neighbor_col, rows, columns):
                min_neighbor_distance = min(
                    min_neighbor_distance,
                    cell_heights[neighbor_row][neighbor_col],
                )

            neighbor_row = row
            neighbor_col = col - 1

            if _is_valid_cell(neighbor_row, neighbor_col, rows, columns):
                min_neighbor_distance = min(
                    min_neighbor_distance,
                    cell_heights[neighbor_row][neighbor_col],
                )

            cell_heights[row][col] = min(
                cell_heights[row][col], min_neighbor_distance + 1
            )

    for row in range(rows - 1, -1, -1):
        for col in range(columns - 1, -1, -1):
            min_neighbor_distance = INF
            neighbor_row = row + 1
            neighbor_col = col

            if _is_valid_cell(neighbor_row, neighbor_col, rows, columns):
                min_neighbor_distance = min(
                    min_neighbor_distance,
                    cell_heights[neighbor_row][neighbor_col],
                )

            neighbor_row = row
            neighbor_col = col + 1
            if _is_valid_cell(neighbor_row, neighbor_col, rows, columns):
                min_neighbor_distance = min(
                    min_neighbor_distance,
                    cell_heights[neighbor_row][neighbor_col],
                )

            cell_heights[row][col] = min(
                cell_heights[row][col], min_neighbor_distance + 1
            )

    return cell_heights


"""
Speed
"""


def _01765_MapOfHighestPeak_2(isWater: List[List[int]]) -> List[List[int]]:
    q = deque()
    n = len(isWater[0])
    m = len(isWater)
    output = [[-1 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if isWater[i][j] == 1:
                output[i][j] = 0
                q.append((i, j))
    while q:
        i, j = q.popleft()
        if 0 < i < m and output[i - 1][j] == -1:
            output[i - 1][j] = output[i][j] + 1
            q.append((i - 1, j))
        if 0 < j < n and output[i][j - 1] == -1:
            output[i][j - 1] = output[i][j] + 1
            q.append((i, j - 1))
        if 0 <= j < n - 1 and output[i][j + 1] == -1:
            output[i][j + 1] = output[i][j] + 1
            q.append((i, j + 1))
        if 0 <= i < m - 1 and output[i + 1][j] == -1:
            output[i + 1][j] = output[i][j] + 1
            q.append((i + 1, j))
    return output


def solve():
    for i in range(ncases):
        res0 = _01765_MapOfHighestPeak_0(v[i])
        for j in res0:
            output.writelines(str.join(" ", [str(k) for k in j]) + "\n")

        res1 = _01765_MapOfHighestPeak_1(v[i])
        for j in res1:
            output.writelines(str.join(" ", [str(k) for k in j]) + "\n")

        res2 = _01765_MapOfHighestPeak_2(v[i])
        for j in res2:
            output.writelines(str.join(" ", [str(k) for k in j]) + "\n")


# endregion


# region Problem Description
"""
You are given an integer matrix isWater of size m x n that represents a map of land 
and water cells.
If isWater[i][j] == 0, cell (i, j) is a land cell.
If isWater[i][j] == 1, cell (i, j) is a water cell.
You must assign each cell a height in a way that follows these rules:
The height of each cell must be non-negative.
If the cell is a water cell, its height must be 0.
Any two adjacent cells must have an absolute height difference of at most 1. 
A cell is adjacent to another cell if the former is directly north, east, south, or west 
of the latter (i.e., their sides are touching).
Find an assignment of heights such that the maximum height in the matrix is maximized.
Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. 
If there are multiple solutions, return any of them.

Constraints:

m == isWater.length
n == isWater[i].length
1 <= m, n <= 1000
isWater[i][j] is 0 or 1.
There is at least one water cell.
"""


def _01765_MapOfHighestPeak():
    os.system("cls")
    data_collector()
    solve()


_01765_MapOfHighestPeak()
# endregion


# region Unit Testing
class _01765_MapOfHighestPeak_Test(unittest.TestCase):
    def test_01765_MapOfHighestPeak_0(self):
        for i in range(ncases):
            self.assertEqual(
                _01765_MapOfHighestPeak_0(v[i]),
                v0[i],
            )

    def test_01765_MapOfHighestPeak_1(self):
        for i in range(ncases):
            self.assertEqual(
                _01765_MapOfHighestPeak_1(v[i]),
                v0[i],
            )

    def test_01765_MapOfHighestPeak_2(self):
        for i in range(ncases):
            self.assertEqual(
                _01765_MapOfHighestPeak_2(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
