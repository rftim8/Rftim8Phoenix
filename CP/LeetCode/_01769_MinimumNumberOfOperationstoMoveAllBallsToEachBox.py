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
        f"{cwd}/Data/CP/LeetCode/IO/_01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_Output.txt",
    "w",
)


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(input[i])
        v0.append(rft_stl.string_to_1D_list_of_int(input[i + 1]))


# endregion


# region Solutions
"""
Brute Force
"""


def _01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_0(boxes: str) -> List[int]:
    res = [0] * len(boxes)

    for current_box in range(len(boxes)):
        if boxes[current_box] == "1":
            for new_position in range(len(boxes)):
                res[new_position] += abs(new_position - current_box)

    return res


"""
Sum Of Left And Right Moves
"""


def _01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_1(boxes: str) -> List[int]:
    n = len(boxes)
    answer = [0] * n

    balls_to_left = 0
    moves_to_left = 0
    balls_to_right = 0
    moves_to_right = 0

    for i in range(n):
        answer[i] += moves_to_left
        balls_to_left += int(boxes[i])
        moves_to_left += balls_to_left
        j = n - 1 - i
        answer[j] += moves_to_right
        balls_to_right += int(boxes[j])
        moves_to_right += balls_to_right

    return answer


"""
Speed
"""


def _01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_2(boxes: str) -> List[int]:
    res = []
    pref = p = s = 0

    for i, el in enumerate(boxes):
        if el == "1":
            pref += i
            p += 1

    for el in boxes:
        res.append(pref)
        if el == "1":
            p -= 1
            s += 1
        pref = pref - p + s

    return res


def solve():
    for i in range(ncases):
        res0 = _01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_1(v[i])
        output.writelines(str(res1) + "\n")

        res2 = _01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_2(v[i])
        output.writelines(str(res2) + "\n")


# endregion


# region Problem Description
"""
You have n boxes. 
You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, 
and '1' if it contains one ball.
In one operation, you can move one ball from a box to an adjacent box. 
Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, 
there may be more than one ball in some boxes.
Return an array answer of size n, where answer[i] is the minimum number of operations needed to move 
all the balls to the ith box.
Each answer[i] is calculated considering the initial state of the boxes.

Constraints:

n == boxes.length
1 <= n <= 2000
boxes[i] is either '0' or '1'.
"""


def _01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox():
    os.system("cls")
    data_collector()
    solve()


_01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox()
# endregion


# region Unit Testing
class _01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_Test(unittest.TestCase):
    def test_01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_0(self):
        for i in range(ncases):
            self.assertEqual(
                _01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_0(v[i]),
                v0[i],
            )

    def test_01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_1(self):
        for i in range(ncases):
            self.assertEqual(
                _01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_1(v[i]),
                v0[i],
            )

    def test_01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_2(self):
        for i in range(ncases):
            self.assertEqual(
                _01769_MinimumNumberOfOperationstoMoveAllBallsToEachBox_2(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
