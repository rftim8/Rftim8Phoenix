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
        f"{cwd}/Data/CP/LeetCode/IO/_02946_MatrixSimilarityAfterCyclicShifts_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02946_MatrixSimilarityAfterCyclicShifts_Output.txt",
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
        v.append(rft_stl.string_to_2D_list_of_int(input[i]))
        v0.append(int(input[i + 1]))
        v1.append(True if input[i + 2] == "true" else False)


# endregion


# region Solutions
"""
"""


def _02946_MatrixSimilarityAfterCyclicShifts_0(mat: List[List[int]], k: int) -> bool:
    mat0 = [i for i in mat]
    y = len(mat)

    for i in range(y):
        for j in range(k):
            mat[i] = [mat[i][-1]] + mat[i][:-1]

    for i in range(y):
        if mat[i] != mat0[i]:
            return False

    return True


def solve():
    for i in range(ncases):
        res0 = _02946_MatrixSimilarityAfterCyclicShifts_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
You are given an m x n integer matrix mat and an integer k. 
The matrix rows are 0-indexed.
The following proccess happens k times:
Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.
Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.
Return true if the final modified matrix after k steps is identical to the original matrix, and false otherwise.

Constraints:

1 <= mat.length <= 25
1 <= mat[i].length <= 25
1 <= mat[i][j] <= 25
1 <= k <= 50
"""


def _02946_MatrixSimilarityAfterCyclicShifts():
    os.system("cls")
    data_collector()
    solve()


_02946_MatrixSimilarityAfterCyclicShifts()
# endregion


# region Unit Testing
class _02946_MatrixSimilarityAfterCyclicShifts_Test(unittest.TestCase):
    def test_02946_MatrixSimilarityAfterCyclicShifts_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02946_MatrixSimilarityAfterCyclicShifts_0(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
