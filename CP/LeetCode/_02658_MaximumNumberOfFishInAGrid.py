# region Imports
from copy import deepcopy
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
    open(f"{cwd}/Data/CP/LeetCode/IO/_02658_MaximumNumberOfFishInAGrid_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02658_MaximumNumberOfFishInAGrid_Output.txt", "w"
)


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
DFS
"""


def _02658_MaximumNumberOfFishInAGrid_0(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    max_fish_count = 0
    visited = [[False] * cols for _ in range(rows)]

    def calculate_fishes(grid, visited, row, col):
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[0])
            or grid[row][col] == 0
            or visited[row][col]
        ):
            return 0

        visited[row][col] = True

        return (
            grid[row][col]
            + calculate_fishes(grid, visited, row, col + 1)
            + calculate_fishes(grid, visited, row, col - 1)
            + calculate_fishes(grid, visited, row + 1, col)
            + calculate_fishes(grid, visited, row - 1, col)
        )

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] > 0 and not visited[row][col]:
                max_fish_count = max(
                    max_fish_count,
                    calculate_fishes(grid, visited, row, col),
                )

    return max_fish_count


"""
BFS
"""


def _02658_MaximumNumberOfFishInAGrid_1(grid: List[List[int]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])
    result = 0
    visited = [[False] * num_cols for _ in range(num_rows)]

    def count_fishes(grid, visited, row, col):
        num_rows = len(grid)
        num_cols = len(grid[0])
        fish_count = 0
        q = [(row, col)]
        visited[row][col] = True
        row_directions = [0, 0, 1, -1]
        col_directions = [1, -1, 0, 0]

        while q:
            row, col = q.pop(0)
            fish_count += grid[row][col]

            for i in range(4):
                new_row = row + row_directions[i]
                new_col = col + col_directions[i]
                if (
                    0 <= new_row < num_rows
                    and 0 <= new_col < num_cols
                    and grid[new_row][new_col]
                    and not visited[new_row][new_col]
                ):
                    q.append((new_row, new_col))
                    visited[new_row][new_col] = True

        return fish_count

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] and not visited[i][j]:
                result = max(result, count_fishes(grid, visited, i, j))

    return result


"""
Union Find
"""


def _02658_MaximumNumberOfFishInAGrid_2(grid: List[List[int]]) -> int:
    def find_parent(cell_index):
        if parent[cell_index] != cell_index:
            parent[cell_index] = find_parent(parent[cell_index])

        return parent[cell_index]

    def union_components(cell_index1, cell_index2):
        root1 = find_parent(cell_index1)
        root2 = find_parent(cell_index2)

        if root1 != root2:
            if component_size[root1] < component_size[root2]:
                root1, root2 = root2, root1

            parent[root2] = root1
            component_size[root1] += component_size[root2]
            total_fish[root1] += total_fish[root2]

    row_count, column_count = len(grid), len(grid[0])
    total_cells = row_count * column_count
    parent = list(range(total_cells))
    component_size = [1] * total_cells
    total_fish = [0] * total_cells

    for row in range(row_count):
        for column in range(column_count):
            cell_index = row * column_count + column
            total_fish[cell_index] = grid[row][column]

    delta_row = [0, 0, 1, -1]
    delta_column = [1, -1, 0, 0]

    for row in range(row_count):
        for column in range(column_count):
            if grid[row][column] > 0:
                cell_index = row * column_count + column

                for direction in range(4):
                    neighbor_row = row + delta_row[direction]
                    neighbor_column = column + delta_column[direction]

                    if (
                        0 <= neighbor_row < row_count
                        and 0 <= neighbor_column < column_count
                        and grid[neighbor_row][neighbor_column] > 0
                    ):
                        neighbor_index = neighbor_row * column_count + neighbor_column
                        union_components(cell_index, neighbor_index)

    max_fish = 0

    for cell_index in range(total_cells):
        if find_parent(cell_index) == cell_index:
            max_fish = max(max_fish, total_fish[cell_index])

    return max_fish


"""
Speed - DFS
"""


def _02658_MaximumNumberOfFishInAGrid_3(grid0: List[List[int]]) -> int:
    res = 0
    grid = deepcopy(grid0)
    nrow, ncol = len(grid), len(grid[0])

    def dfs(grid, i, j):
        nrow, ncol = len(grid), len(grid[0])

        if i < 0 or j < 0 or i >= nrow or j >= ncol:
            return 0

        if grid[i][j] == 0:
            return 0

        temp = grid[i][j]
        grid[i][j] = 0

        return (
            temp
            + dfs(grid, i + 1, j)
            + dfs(grid, i - 1, j)
            + dfs(grid, i, j + 1)
            + dfs(grid, i, j - 1)
        )

    for i in range(nrow):
        for j in range(ncol):
            if grid[i][j] != 0:
                res = max(res, dfs(grid, i, j))

    return res


def solve():
    for i in range(ncases):
        res0 = _02658_MaximumNumberOfFishInAGrid_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _02658_MaximumNumberOfFishInAGrid_1(v[i])
        output.writelines(str(res1) + "\n")

        res2 = _02658_MaximumNumberOfFishInAGrid_2(v[i])
        output.writelines(str(res2) + "\n")

        res3 = _02658_MaximumNumberOfFishInAGrid_3(v[i])
        output.writelines(str(res3) + "\n")


# endregion


# region Problem Description
"""
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations 
any number of times:
Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell 
optimally, or 0 if no water cell exists.
An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) 
or (r - 1, c) if it exists.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10
"""


def _02658_MaximumNumberOfFishInAGrid():
    os.system("cls")
    data_collector()
    solve()


_02658_MaximumNumberOfFishInAGrid()
# endregion


# region Unit Testing
class _02658_MaximumNumberOfFishInAGrid_Test(unittest.TestCase):
    def test_02658_MaximumNumberOfFishInAGrid_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02658_MaximumNumberOfFishInAGrid_0(v[i]),
                v0[i],
            )

    def test_02658_MaximumNumberOfFishInAGrid_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02658_MaximumNumberOfFishInAGrid_1(v[i]),
                v0[i],
            )

    def test_02658_MaximumNumberOfFishInAGrid_2(self):
        for i in range(ncases):
            self.assertEqual(
                _02658_MaximumNumberOfFishInAGrid_2(v[i]),
                v0[i],
            )

    def test_02658_MaximumNumberOfFishInAGrid_3(self):
        for i in range(ncases):
            self.assertEqual(
                _02658_MaximumNumberOfFishInAGrid_3(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
