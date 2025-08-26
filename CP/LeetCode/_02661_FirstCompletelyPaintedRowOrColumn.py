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
        f"{cwd}/Data/CP/LeetCode/IO/_02661_FirstCompletelyPaintedRowOrColumn_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02661_FirstCompletelyPaintedRowOrColumn_Output.txt",
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
        v0.append(rft_stl.string_to_2D_list_of_int(input[i + 1]))
        v1.append(int(input[i + 2]))


# endregion


# region Solutions
"""
Brute Force optimized solution
"""


def _02661_FirstCompletelyPaintedRowOrColumn_0(
    arr: List[int], mat: List[List[int]]
) -> int:
    num_rows, num_cols = len(mat), len(mat[0])
    row_count, col_count = [0] * num_rows, [0] * num_cols
    num_to_pos = {}

    for row in range(num_rows):
        for col in range(num_cols):
            num_to_pos[mat[row][col]] = [row, col]

    for i in range(len(arr)):
        num = arr[i]
        row, col = num_to_pos[num]

        row_count[row] += 1
        col_count[col] += 1

        if row_count[row] == num_cols or col_count[col] == num_rows:
            return i

    return -1


"""
Revere Mapping
"""


def _02661_FirstCompletelyPaintedRowOrColumn_1(
    arr: List[int], mat: List[List[int]]
) -> int:
    num_to_index = {}
    for i in range(len(arr)):
        num_to_index[arr[i]] = i

    result = float("inf")
    num_rows, num_cols = len(mat), len(mat[0])

    for row in range(num_rows):
        last_element_index = float("-inf")

        for col in range(num_cols):
            index_val = num_to_index[mat[row][col]]
            last_element_index = max(last_element_index, index_val)

        result = min(result, last_element_index)

    for col in range(num_cols):
        last_element_index = float("-inf")

        for row in range(num_rows):
            index_val = num_to_index[mat[row][col]]
            last_element_index = max(last_element_index, index_val)

        result = min(result, last_element_index)

    return result


"""
Speed
"""


def _02661_FirstCompletelyPaintedRowOrColumn_2(
    arr: List[int], mat: List[List[int]]
) -> int:
    m = len(mat)
    n = len(mat[0])
    rows = [0] * m
    cols = [0] * n
    numToRow = [0] * (m * n + 1)
    numToCol = [0] * (m * n + 1)

    for i, row in enumerate(mat):
        for j, num in enumerate(row):
            numToRow[num] = i
            numToCol[num] = j

    for i, a in enumerate(arr):
        rows[numToRow[a]] += 1

        if rows[numToRow[a]] == n:
            return i
        cols[numToCol[a]] += 1

        if cols[numToCol[a]] == m:
            return i


def solve():
    for i in range(ncases):
        res0 = _02661_FirstCompletelyPaintedRowOrColumn_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")

        res1 = _02661_FirstCompletelyPaintedRowOrColumn_1(v[i], v0[i])
        output.writelines(str(res1) + "\n")

        res2 = _02661_FirstCompletelyPaintedRowOrColumn_2(v[i], v0[i])
        output.writelines(str(res2) + "\n")


# endregion


# region Problem Description
"""
You are given a 0-indexed integer array arr, and an m x n integer matrix mat. 
arr and mat both contain all the integers in the range [1, m * n].
Go through each index i in arr starting from index 0 and paint the cell in mat 
containing the integer arr[i].
Return the smallest index i at which either a row or a column will be completely 
painted in mat.

Constraints:

m == mat.length
n = mat[i].length
arr.length == m * n
1 <= m, n <= 10^5
1 <= m * n <= 10^5
1 <= arr[i], mat[r][c] <= m * n
All the integers of arr are unique.
All the integers of mat are unique.
"""


def _02661_FirstCompletelyPaintedRowOrColumn():
    os.system("cls")
    data_collector()
    solve()


_02661_FirstCompletelyPaintedRowOrColumn()
# endregion


# region Unit Testing
class _02661_FirstCompletelyPaintedRowOrColumn_Test(unittest.TestCase):
    def test_02661_FirstCompletelyPaintedRowOrColumn_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02661_FirstCompletelyPaintedRowOrColumn_0(v[i], v0[i]),
                v1[i],
            )

    def test_02661_FirstCompletelyPaintedRowOrColumn_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02661_FirstCompletelyPaintedRowOrColumn_1(v[i], v0[i]),
                v1[i],
            )

    def test_02661_FirstCompletelyPaintedRowOrColumn_2(self):
        for i in range(ncases):
            self.assertEqual(
                _02661_FirstCompletelyPaintedRowOrColumn_2(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
