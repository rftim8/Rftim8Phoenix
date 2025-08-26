# region Imports
import collections
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
    open(
        f"{cwd}/Data/CP/LeetCode/IO/_01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_Output.txt",
    "w",
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
DP
"""


def _01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_0(grid: List[List[int]]) -> int:
    num_rows, num_cols = len(grid), len(grid[0])
    min_changes = [[float("inf")] * num_cols for _ in range(num_rows)]
    min_changes[0][0] = 0

    while True:
        prev_state = [row[:] for row in min_changes]

        for row in range(num_rows):
            for col in range(num_cols):
                if row > 0:
                    min_changes[row][col] = min(
                        min_changes[row][col],
                        min_changes[row - 1][col]
                        + (0 if grid[row - 1][col] == 3 else 1),
                    )

                if col > 0:
                    min_changes[row][col] = min(
                        min_changes[row][col],
                        min_changes[row][col - 1]
                        + (0 if grid[row][col - 1] == 1 else 1),
                    )

        for row in range(num_rows - 1, -1, -1):
            for col in range(num_cols - 1, -1, -1):
                if row < num_rows - 1:
                    min_changes[row][col] = min(
                        min_changes[row][col],
                        min_changes[row + 1][col]
                        + (0 if grid[row + 1][col] == 4 else 1),
                    )

                if col < num_cols - 1:
                    min_changes[row][col] = min(
                        min_changes[row][col],
                        min_changes[row][col + 1]
                        + (0 if grid[row][col + 1] == 2 else 1),
                    )
        if min_changes == prev_state:
            break

    return min_changes[num_rows - 1][num_cols - 1]


"""
Dijkstra's Algorithm
"""


def _01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_1(
    grid: List[List[int]],
) -> int:
    _dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    num_rows, num_cols = len(grid), len(grid[0])

    pq = [(0, 0, 0)]
    min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]
    min_cost[0][0] = 0

    while pq:
        cost, row, col = heapq.heappop(pq)

        if min_cost[row][col] != cost:
            continue

        for d, (dx, dy) in enumerate(_dirs):
            new_row, new_col = row + dx, col + dy

            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                new_cost = cost + (d != (grid[row][col] - 1))

                if min_cost[new_row][new_col] > new_cost:
                    min_cost[new_row][new_col] = new_cost
                    heapq.heappush(pq, (new_cost, new_row, new_col))

    return min_cost[num_rows - 1][num_cols - 1]


"""
0/1 BFS
"""


def _is_valid(row: int, col: int, num_rows: int, num_cols: int) -> bool:
    return 0 <= row < num_rows and 0 <= col < num_cols


def _01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_2(
    grid: List[List[int]],
) -> int:
    _dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    num_rows, num_cols = len(grid), len(grid[0])
    min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]
    min_cost[0][0] = 0

    deque = collections.deque([(0, 0)])

    while deque:
        row, col = deque.popleft()

        for dir_idx, (dx, dy) in enumerate(_dirs):
            new_row, new_col = row + dx, col + dy
            cost = 0 if grid[row][col] == dir_idx + 1 else 1

            if (
                _is_valid(new_row, new_col, num_rows, num_cols)
                and min_cost[row][col] + cost < min_cost[new_row][new_col]
            ):

                min_cost[new_row][new_col] = min_cost[row][col] + cost

                if cost == 1:
                    deque.append((new_row, new_col))
                else:
                    deque.appendleft((new_row, new_col))

    return min_cost[num_rows - 1][num_cols - 1]


"""
DFS + BFS
"""

_dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def _is_unvisited(min_cost: List[List[int]], row: int, col: int) -> bool:
    return (
        0 <= row < len(min_cost)
        and 0 <= col < len(min_cost[0])
        and min_cost[row][col] == float("inf")
    )


def _dfs(
    grid: List[List[int]],
    row: int,
    col: int,
    min_cost: List[List[int]],
    cost: int,
    queue: collections.deque,
) -> None:
    if not _is_unvisited(min_cost, row, col):
        return

    min_cost[row][col] = cost
    queue.append((row, col))
    next_dir = grid[row][col] - 1
    dx, dy = _dirs[next_dir]
    _dfs(grid, row + dx, col + dy, min_cost, cost, queue)


def _01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_3(
    grid: List[List[int]],
) -> int:
    num_rows, num_cols = len(grid), len(grid[0])
    cost = 0
    min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]
    queue = collections.deque()
    _dfs(grid, 0, 0, min_cost, cost, queue)

    while queue:
        cost += 1
        level_size = len(queue)

        for _ in range(level_size):
            row, col = queue.popleft()

            for dir_idx, (dx, dy) in enumerate(_dirs):
                _dfs(grid, row + dx, col + dy, min_cost, cost, queue)

    return min_cost[num_rows - 1][num_cols - 1]


def solve():
    for i in range(ncases):
        res0 = _01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_1(v[i])
        output.writelines(str(res1) + "\n")

        res2 = _01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_2(v[i])
        output.writelines(str(res2) + "\n")

        res3 = _01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_3(v[i])
        output.writelines(str(res3) + "\n")


# endregion


# region Problem Description
"""
Given an m x n grid. 
Each cell of the grid has a sign pointing to the next cell you should visit if you are 
currently in this cell. 
The sign of grid[i][j] can be:
1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some signs on the cells of the grid that point outside the grid.
You will initially start at the upper left cell (0, 0). 
A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends 
at the bottom-right cell (m - 1, n - 1) following the signs on the grid. 
The valid path does not have to be the shortest.
You can modify the sign on a cell with cost = 1. 
You can modify the sign on a cell one time only.
Return the minimum cost to make the grid have at least one valid path.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
1 <= grid[i][j] <= 4
"""


def _01368_MinimumCostToMakeAtLeastOneValidPathInAGrid():
    os.system("cls")
    data_collector()
    solve()


_01368_MinimumCostToMakeAtLeastOneValidPathInAGrid()
# endregion


# region Unit Testing
class _01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_Test(unittest.TestCase):
    def test_01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_0(self):
        for i in range(ncases):
            self.assertEqual(
                _01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_0(v[i]),
                v0[i],
            )

    def test_01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_1(self):
        for i in range(ncases):
            self.assertEqual(
                _01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_1(v[i]),
                v0[i],
            )

    def test_01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_2(self):
        for i in range(ncases):
            self.assertEqual(
                _01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_2(v[i]),
                v0[i],
            )

    def test_01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_3(self):
        for i in range(ncases):
            self.assertEqual(
                _01368_MinimumCostToMakeAtLeastOneValidPathInAGrid_3(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
