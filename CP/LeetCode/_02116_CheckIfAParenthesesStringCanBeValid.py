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
        f"{cwd}/Data/CP/LeetCode/IO/_02116_CheckIfAParenthesesStringCanBeValid_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02116_CheckIfAParenthesesStringCanBeValid_Output.txt",
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
        v.append(input[i])
        v0.append(input[i + 1])
        v1.append(True if input[i + 2] == "true" else False)


# endregion


# region Solutions
"""
Stack
"""


def _02116_CheckIfAParenthesesStringCanBeValid_0(s: str, locked: str) -> bool:
    length = len(s)

    if length % 2 == 1:
        return False

    open_brackets = []
    unlocked = []

    for i in range(length):
        if locked[i] == "0":
            unlocked.append(i)
        elif s[i] == "(":
            open_brackets.append(i)
        elif s[i] == ")":
            if open_brackets:
                open_brackets.pop()
            elif unlocked:
                unlocked.pop()
            else:
                return False

    while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
        open_brackets.pop()
        unlocked.pop()

    if open_brackets:
        return False

    return True


"""
Constant Space
"""


def _02116_CheckIfAParenthesesStringCanBeValid_1(s: str, locked: str) -> bool:
    length = len(s)

    if length % 2 == 1:
        return False

    open_brackets = 0
    unlocked_count = 0

    for i in range(length):
        if locked[i] == "0":
            unlocked_count += 1
        elif s[i] == "(":
            open_brackets += 1
        elif s[i] == ")":
            if open_brackets > 0:
                open_brackets -= 1
            elif unlocked_count > 0:
                unlocked_count -= 1
            else:
                return False

    balance_count = 0

    for i in range(length - 1, -1, -1):
        if locked[i] == "0":
            balance_count -= 1
            unlocked_count -= 1
        elif s[i] == "(":
            balance_count += 1
            open_brackets -= 1
        elif s[i] == ")":
            balance_count -= 1
        if balance_count > 0:
            return False
        if unlocked_count == 0 and open_brackets == 0:
            break

    if open_brackets > 0:
        return False

    return True


def solve():
    for i in range(ncases):
        res0 = _02116_CheckIfAParenthesesStringCanBeValid_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")

        res1 = _02116_CheckIfAParenthesesStringCanBeValid_1(v[i], v0[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
A parentheses string is a non-empty string consisting only of '(' and ')'. 
It is valid if any of the following conditions is true:
It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. 
locked is a binary string consisting only of '0's and '1's. For each index i of locked,
If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.

Constraints:

n == s.length == locked.length
1 <= n <= 105
s[i] is either '(' or ')'.
locked[i] is either '0' or '1'.
"""


def _02116_CheckIfAParenthesesStringCanBeValid():
    os.system("cls")
    data_collector()
    solve()


_02116_CheckIfAParenthesesStringCanBeValid()
# endregion


# region Unit Testing
class _02116_CheckIfAParenthesesStringCanBeValid_Test(unittest.TestCase):
    def test_02116_CheckIfAParenthesesStringCanBeValid_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02116_CheckIfAParenthesesStringCanBeValid_0(v[i], v0[i]),
                v1[i],
            )

    def test_02116_CheckIfAParenthesesStringCanBeValid_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02116_CheckIfAParenthesesStringCanBeValid_1(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
