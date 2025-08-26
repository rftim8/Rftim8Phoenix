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
    open(f"{cwd}/Data/CP/LeetCode/IO/_01267_CountServersThatCommunicate_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_01267_CountServersThatCommunicate_Output.txt", "w"
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
Brute Force Solution
"""


def _01267_CountServersThatCommunicate_0(grid: List[List[int]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows > 0 else 0
    communicable_servers_count = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1:
                can_communicate = False

                for other_col in range(num_cols):
                    if other_col != col and grid[row][other_col] == 1:
                        can_communicate = True
                        break

                if can_communicate:
                    communicable_servers_count += 1
                else:
                    for other_row in range(num_rows):
                        if other_row != row and grid[other_row][col] == 1:
                            can_communicate = True
                            break

                    if can_communicate:
                        communicable_servers_count += 1

    return communicable_servers_count


"""
Track Using Two Arrays
"""


def _01267_CountServersThatCommunicate_1(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    row_counts = [0] * len(grid[0])
    col_counts = [0] * len(grid)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                row_counts[col] += 1
                col_counts[row] += 1

    communicable_servers_count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                if row_counts[col] > 1 or col_counts[row] > 1:
                    communicable_servers_count += 1

    return communicable_servers_count


"""
Server Grouping
"""


def _01267_CountServersThatCommunicate_2(grid: List[List[int]]) -> int:
    res = 0
    row_counts = [0] * len(grid[0])
    last_server_in_col = [-1] * len(grid)

    for row in range(len(grid)):
        server_count_in_row = 0
        for col in range(len(grid[0])):
            if grid[row][col]:
                server_count_in_row += 1
                row_counts[col] += 1
                last_server_in_col[row] = col

        if server_count_in_row != 1:
            res += server_count_in_row
            last_server_in_col[row] = -1

    for row in range(len(grid)):
        if last_server_in_col[row] != -1 and row_counts[last_server_in_col[row]] > 1:
            res += 1

    return res


"""
Speed
"""


def _01267_CountServersThatCommunicate_3(grid: List[List[int]]) -> int:
    count = 0

    for r in range(len(grid)):
        s = sum(grid[r])
        if s > 1:
            count += s
        elif s == 1:
            column = grid[r].index(1)
            if sum(grid[r][column] for r in range(len(grid))) > 1:
                count += 1

    return count


def solve():
    for i in range(ncases):
        res0 = _01267_CountServersThatCommunicate_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _01267_CountServersThatCommunicate_1(v[i])
        output.writelines(str(res1) + "\n")

        res2 = _01267_CountServersThatCommunicate_2(v[i])
        output.writelines(str(res2) + "\n")

        res3 = _01267_CountServersThatCommunicate_3(v[i])
        output.writelines(str(res3) + "\n")


# endregion


# region Problem Description
"""
You are given a map of a server center, represented as a m * n integer matrix grid, 
where 1 means that on that cell there is a server and 0 means that it is no server. 
Two servers are said to communicate if they are on the same row or on the same column.
Return the number of servers that communicate with any other server.

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
"""


def _01267_CountServersThatCommunicate():
    os.system("cls")
    data_collector()
    solve()


_01267_CountServersThatCommunicate()
# endregion


# region Unit Testing
class _01267_CountServersThatCommunicate_Test(unittest.TestCase):
    def test_01267_CountServersThatCommunicate_0(self):
        for i in range(ncases):
            self.assertEqual(
                _01267_CountServersThatCommunicate_0(v[i]),
                v0[i],
            )

    def test_01267_CountServersThatCommunicate_1(self):
        for i in range(ncases):
            self.assertEqual(
                _01267_CountServersThatCommunicate_1(v[i]),
                v0[i],
            )

    def test_01267_CountServersThatCommunicate_2(self):
        for i in range(ncases):
            self.assertEqual(
                _01267_CountServersThatCommunicate_2(v[i]),
                v0[i],
            )

    def test_01267_CountServersThatCommunicate_3(self):
        for i in range(ncases):
            self.assertEqual(
                _01267_CountServersThatCommunicate_3(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
