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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00827_MakingALargeIsland_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_00827_MakingALargeIsland_Output.txt", "w")


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


def _00827_MakingALargeIsland_0(grid0: List[List[int]]) -> int:
    def dfs(x, y, identifier, grid, n):
        stack = [(x, y)]
        grid[x][y] = -1
        island = []
        size = 0

        while stack:
            x_current, y_current = stack.pop()
            island.append((x_current, y_current))
            size += 1

            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x_n, y_n = x_current + d[0], y_current + d[1]

                if 0 <= x_n < n and 0 <= y_n < n and grid[x_n][y_n] == 1:
                    grid[x_n][y_n] = -1
                    stack.append((x_n, y_n))

        for x, y in island:
            land2size[(x, y)] = (identifier, size)

    def getSize(x, y, grid, n):
        size = 1
        visited = set()

        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x_n, y_n = x + d[0], y + d[1]

            if 0 <= x_n < n and 0 <= y_n < n and grid[x_n][y_n] == -1:
                if land2size[(x_n, y_n)][0] not in visited:
                    size += land2size[(x_n, y_n)][1]
                    visited.add(land2size[(x_n, y_n)][0])

        return size

    land2size = {}
    grid = deepcopy(grid0)
    n = len(grid)
    identifier = 0

    for x in range(n):
        for y in range(n):
            if grid[x][y] == 1:
                dfs(x, y, identifier, grid, n)
                identifier += 1
    if not land2size:
        return 1
    else:
        res = max([size for _, size in land2size.values()])

    for x in range(n):
        for y in range(n):
            if grid[x][y] == 0:
                res = max(res, getSize(x, y, grid, n))

    return res


"""
DFS
"""


def _00827_MakingALargeIsland_1(grid0: List[List[int]]) -> int:
    grid = deepcopy(grid0)

    def explore_island(
        grid: List[List[int]],
        island_id: int,
        current_row: int,
        current_column: int,
    ) -> int:
        if (
            current_row < 0
            or current_row >= len(grid)
            or current_column < 0
            or current_column >= len(grid[0])
            or grid[current_row][current_column] != 1
        ):
            return 0

        grid[current_row][current_column] = island_id

        return (
            1
            + explore_island(grid, island_id, current_row + 1, current_column)
            + explore_island(grid, island_id, current_row - 1, current_column)
            + explore_island(grid, island_id, current_row, current_column + 1)
            + explore_island(grid, island_id, current_row, current_column - 1)
        )

    island_sizes = {}
    island_id = 2

    for current_row in range(len(grid)):
        for current_column in range(len(grid[0])):
            if grid[current_row][current_column] == 1:
                island_sizes[island_id] = explore_island(
                    grid, island_id, current_row, current_column
                )
                island_id += 1

    if not island_sizes:
        return 1

    if len(island_sizes) == 1:
        island_id -= 1

        return (
            island_sizes[island_id]
            if island_sizes[island_id] == len(grid) * len(grid[0])
            else island_sizes[island_id] + 1
        )

    max_island_size = 1

    for current_row in range(len(grid)):
        for current_column in range(len(grid[0])):
            if grid[current_row][current_column] == 0:
                current_island_size = 1
                neighboring_islands = set()

                if (
                    current_row + 1 < len(grid)
                    and grid[current_row + 1][current_column] > 1
                ):
                    neighboring_islands.add(grid[current_row + 1][current_column])

                if current_row - 1 >= 0 and grid[current_row - 1][current_column] > 1:
                    neighboring_islands.add(grid[current_row - 1][current_column])

                if (
                    current_column + 1 < len(grid[0])
                    and grid[current_row][current_column + 1] > 1
                ):
                    neighboring_islands.add(grid[current_row][current_column + 1])

                if (
                    current_column - 1 >= 0
                    and grid[current_row][current_column - 1] > 1
                ):
                    neighboring_islands.add(grid[current_row][current_column - 1])

                for island_id in neighboring_islands:
                    current_island_size += island_sizes[island_id]

                max_island_size = max(max_island_size, current_island_size)

    return max_island_size


"""
DSU - Dsijo Set Union
"""


def _00827_MakingALargeIsland_2(grid: List[List[int]]) -> int:
    class DisjointSet:
        def __init__(self, n: int):
            self.parent = [i for i in range(n)]
            self.island_size = [1] * n

        def find_root(self, node: int) -> int:

            if self.parent[node] == node:
                return node

            self.parent[node] = self.find_root(self.parent[node])

            return self.parent[node]

        def union_nodes(self, node_a: int, node_b: int):
            root_a = self.find_root(node_a)
            root_b = self.find_root(node_b)

            if root_a == root_b:
                return

            if self.island_size[root_a] < self.island_size[root_b]:
                self.parent[root_a] = root_b
                self.island_size[root_b] += self.island_size[root_a]
            else:
                self.parent[root_b] = root_a
                self.island_size[root_a] += self.island_size[root_b]

    rows = len(grid)
    columns = len(grid[0])
    ds = DisjointSet(rows * columns)
    row_directions = [1, -1, 0, 0]
    column_directions = [0, 0, 1, -1]

    for current_row in range(rows):
        for current_column in range(columns):
            if grid[current_row][current_column] == 1:
                current_node = (columns * current_row) + current_column

                for direction in range(4):
                    neighbor_row = current_row + row_directions[direction]
                    neighbor_column = current_column + column_directions[direction]

                    if (
                        0 <= neighbor_row < rows
                        and 0 <= neighbor_column < columns
                        and grid[neighbor_row][neighbor_column] == 1
                    ):
                        neighbor_node = columns * neighbor_row + neighbor_column
                        ds.union_nodes(current_node, neighbor_node)

    max_island_size = 0
    has_zero = False
    unique_roots = set()

    for current_row in range(rows):
        for current_column in range(columns):
            if grid[current_row][current_column] == 0:
                has_zero = True
                current_island_size = 1

                for direction in range(4):
                    neighbor_row = current_row + row_directions[direction]
                    neighbor_column = current_column + column_directions[direction]

                    if (
                        0 <= neighbor_row < rows
                        and 0 <= neighbor_column < columns
                        and grid[neighbor_row][neighbor_column] == 1
                    ):
                        neighbor_node = columns * neighbor_row + neighbor_column
                        root = ds.find_root(neighbor_node)
                        unique_roots.add(root)

                for root in unique_roots:
                    current_island_size += ds.island_size[root]

                unique_roots.clear()
                max_island_size = max(max_island_size, current_island_size)

    if not has_zero:
        return rows * columns

    return max_island_size


"""
Speed
"""


def _00827_MakingALargeIsland_3(grid0: List[List[int]]) -> int:
    grid = deepcopy(grid0)
    n = len(grid)
    id = 2
    sz = {}

    def dfs(row, col, isl_id):
        grid[row][col] = isl_id
        size = 1

        if row != 0:
            if grid[row - 1][col] == 1:
                size += dfs(row - 1, col, isl_id)
        if col != 0:
            if grid[row][col - 1] == 1:
                size += dfs(row, col - 1, isl_id)
        if row != n - 1:
            if grid[row + 1][col] == 1:
                size += dfs(row + 1, col, isl_id)
        if col != n - 1:
            if grid[row][col + 1] == 1:
                size += dfs(row, col + 1, isl_id)

        return size

    for i in range(n):
        for j in range(n):
            ts = 0
            if grid[i][j] == 1:
                ts = dfs(i, j, id)
                sz[id] = ts
                id += 1

    if not sz:
        return 1

    res = max(sz.values())

    for i in range(n):
        for j in range(n):

            if grid[i][j] == 0:
                sn = set()
                p = 1

                if i != 0:
                    if grid[i - 1][j] > 1:
                        t = grid[i - 1][j]
                        if t not in sn:
                            p += sz[t]
                            sn.add(t)

                if i != n - 1:
                    if grid[i + 1][j] > 1:
                        t = grid[i + 1][j]
                        if t not in sn:
                            p += sz[t]
                            sn.add(t)

                if j != 0:
                    if grid[i][j - 1] > 1:
                        t = grid[i][j - 1]
                        if t not in sn:
                            p += sz[t]
                            sn.add(t)

                if j != n - 1:
                    if grid[i][j + 1] > 1:
                        t = grid[i][j + 1]
                        if t not in sn:
                            p += sz[t]
                            sn.add(t)

                res = max(res, p)
    return res


def solve():
    for i in range(ncases):
        res0 = _00827_MakingALargeIsland_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _00827_MakingALargeIsland_1(v[i])
        output.writelines(str(res1) + "\n")

        res2 = _00827_MakingALargeIsland_2(v[i])
        output.writelines(str(res2) + "\n")

        res3 = _00827_MakingALargeIsland_3(v[i])
        output.writelines(str(res3) + "\n")


# endregion


# region Problem Description
"""
You are given an n x n binary matrix grid. 
You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
"""


def _00827_MakingALargeIsland():
    os.system("cls")
    data_collector()
    solve()


_00827_MakingALargeIsland()
# endregion


# region Unit Testing
class _00827_MakingALargeIsland_Test(unittest.TestCase):
    def test_00827_MakingALargeIsland_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00827_MakingALargeIsland_0(v[i]),
                v0[i],
            )

    def test_00827_MakingALargeIsland_1(self):
        for i in range(ncases):
            self.assertEqual(
                _00827_MakingALargeIsland_1(v[i]),
                v0[i],
            )

    def test_00827_MakingALargeIsland_2(self):
        for i in range(ncases):
            self.assertEqual(
                _00827_MakingALargeIsland_2(v[i]),
                v0[i],
            )

    def test_00827_MakingALargeIsland_3(self):
        for i in range(ncases):
            self.assertEqual(
                _00827_MakingALargeIsland_3(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
