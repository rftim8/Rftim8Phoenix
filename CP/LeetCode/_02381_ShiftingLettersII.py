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
    open(f"{cwd}/Data/CP/LeetCode/IO/_02381_ShiftingLettersII_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_02381_ShiftingLettersII_Output.txt", "w")


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []
v1 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(input[i])
        v0.append(rft_stl.string_to_2D_list_of_int(input[i + 1]))
        v1.append(input[i + 2])


# endregion


# region Solutions
"""
Difference Array
"""


def _02381_ShiftingLettersII_0(s: str, shifts: List[List[int]]) -> str:
    n = len(s)
    diff_array = [0] * n

    for shift in shifts:
        if shift[2] == 1:
            diff_array[shift[0]] += 1
            if shift[1] + 1 < n:
                diff_array[shift[1] + 1] -= 1
        else:
            diff_array[shift[0]] -= 1
            if shift[1] + 1 < n:
                diff_array[shift[1] + 1] += 1

    result = list(s)
    number_of_shifts = 0

    for i in range(n):
        number_of_shifts = (number_of_shifts + diff_array[i]) % 26
        if number_of_shifts < 0:
            number_of_shifts += 26

        shifted_char = chr((ord(s[i]) - ord("a") + number_of_shifts) % 26 + ord("a"))
        result[i] = shifted_char

    return "".join(result)


"""
Difference Array - Optimized
"""


def _02381_ShiftingLettersII_1(s: str, shifts: List[List[int]]) -> str:
    cum_shifts = [0] * (len(s) + 1)

    for st, en, d in shifts:
        if d == 0:
            cum_shifts[st] -= 1
            cum_shifts[en + 1] += 1
        else:
            cum_shifts[st] += 1
            cum_shifts[en + 1] -= 1

    cum_sum = 0
    s = list(s)
    for i in range(len(s)):
        cum_sum += cum_shifts[i]

        new_code = (((ord(s[i]) + cum_sum) - 97) % 26) + 97
        s[i] = chr(new_code)

    return "".join(s)


def solve():
    for i in range(ncases):
        res0 = _02381_ShiftingLettersII_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")

        res1 = _02381_ShiftingLettersII_1(v[i], v0[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
You are given a string s of lowercase English letters and a 2D integer array shifts where 
shifts[i] = [starti, endi, directioni]. 
For every i, shift the characters in s from the index starti to the index endi (inclusive) 
forward if directioni = 1, or shift the characters backward if directioni = 0.
Shifting a character forward means replacing it with the next letter in the 
alphabet (wrapping around so that 'z' becomes 'a'). 
Similarly, shifting a character backward means replacing it with the previous letter in the 
alphabet (wrapping around so that 'a' becomes 'z').
Return the final string after all such shifts to s are applied.

Constraints:

1 <= s.length, shifts.length <= 5 * 10^4
shifts[i].length == 3
0 <= starti <= endi < s.length
0 <= directioni <= 1
s consists of lowercase English letters.
"""


def _02381_ShiftingLettersII():
    os.system("cls")
    data_collector()
    solve()


_02381_ShiftingLettersII()
# endregion


# region Unit Testing
class _02381_ShiftingLettersII_Test(unittest.TestCase):
    def test_02381_ShiftingLettersII_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02381_ShiftingLettersII_0(v[i], v0[i]),
                v1[i],
            )

    def test_02381_ShiftingLettersII_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02381_ShiftingLettersII_1(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
