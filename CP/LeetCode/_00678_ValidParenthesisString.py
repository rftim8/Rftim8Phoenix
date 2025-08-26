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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00678_ValidParenthesisString_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_00678_ValidParenthesisString_Output.txt", "w"
)


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(input[i])
        v0.append(True if input[i + 1] == "true" else False)


# endregion


# region Solutions
"""
"""


def _00678_ValidParenthesisString_0(s: str) -> bool:
    open_count = 0
    close_count = 0
    length = len(s) - 1

    for i in range(length + 1):
        if s[i] == "(" or s[i] == "*":
            open_count += 1
        else:
            open_count -= 1

        if s[length - i] == ")" or s[length - i] == "*":
            close_count += 1
        else:
            close_count -= 1

        if open_count < 0 or close_count < 0:
            return False

    return True


def solve():
    for i in range(ncases):
        res0 = _00678_ValidParenthesisString_0(v[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""


def _00678_ValidParenthesisString():
    os.system("cls")
    data_collector()
    solve()


_00678_ValidParenthesisString()
# endregion


# region Unit Testing
class _00678_ValidParenthesisString_Test(unittest.TestCase):
    def test_00678_ValidParenthesisString_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00678_ValidParenthesisString_0(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
