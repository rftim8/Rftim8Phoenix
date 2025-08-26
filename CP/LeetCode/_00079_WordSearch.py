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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00079_WordSearch_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_00079_WordSearch_Output.txt", "w")


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []
v1 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(rft_stl.string_to_2D_list_of_string(input[i]))
        v0.append(input[i + 1])
        v1.append(True if input[i + 2] == "true" else False)


# endregion


# region Solutions
"""
"""


def Dfs(
    i: int, j: int, start: int, word: str, m: int, n: int, board: List[List[str]]
) -> bool:
    if start == len(word):
        return True

    if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[start]:
        return False

    c = board[i][j]
    board[i][j] = "1"
    result = (
        Dfs(i + 1, j, start + 1, word, m, n, board)
        or Dfs(i - 1, j, start + 1, word, m, n, board)
        or Dfs(i, j + 1, start + 1, word, m, n, board)
        or Dfs(i, j - 1, start + 1, word, m, n, board)
    )
    board[i][j] = c

    return result


def _00079_WordSearch_0(board: List[List[str]], word: str) -> bool:
    m = len(board)
    n = len(board[0])

    for i in range(m):
        for j in range(n):
            if Dfs(i, j, 0, word, m, n, board):
                return True

    return False


def solve():
    for i in range(ncases):
        res0 = _00079_WordSearch_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""


def _00079_WordSearch():
    os.system("cls")
    data_collector()
    solve()


_00079_WordSearch()
# endregion


# region Unit Testing
class _00079_WordSearch_Test(unittest.TestCase):
    def test_00079_WordSearch_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00079_WordSearch_0(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
