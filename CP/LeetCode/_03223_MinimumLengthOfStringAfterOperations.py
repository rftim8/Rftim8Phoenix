# region Imports
import os
from typing import Counter, List
import unittest
import sys

cwd = os.getcwd()
sys.path.append(cwd)
import rft_stl

# endregion


# region Data Gethering
input = (
    open(
        f"{cwd}/Data/CP/LeetCode/IO/_03223_MinimumLengthOfStringAfterOperations_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_03223_MinimumLengthOfStringAfterOperations_Output.txt",
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
        v0.append(int(input[i + 1]))


# endregion


# region Solutions
"""
Hash Map
"""


def _03223_MinimumLengthOfStringAfterOperations_0(s: str) -> int:
    char_frequency_map = Counter(s)
    delete_count = 0

    for frequency in char_frequency_map.values():
        if frequency % 2 == 1:
            delete_count += frequency - 1
        else:
            delete_count += frequency - 2

    return len(s) - delete_count


"""
Frequency Array
"""


def _03223_MinimumLengthOfStringAfterOperations_1(s: str) -> int:
    char_frequency = [0] * 26
    total_length = 0

    for current_char in s:
        char_frequency[ord(current_char) - ord("a")] += 1

    for frequency in char_frequency:
        if frequency == 0:
            continue

        if frequency % 2 == 0:
            total_length += 2
        else:
            total_length += 1

    return total_length


"""
Speed
"""


def _03223_MinimumLengthOfStringAfterOperations_2(s: str) -> int:
    s_set = {
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    }
    ans = 0

    for ch in s_set:
        count = s.count(ch)
        if count & 1:
            ans += 1
        elif count != 0:
            ans += 2

    return ans


def solve():
    for i in range(ncases):
        res0 = _03223_MinimumLengthOfStringAfterOperations_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _03223_MinimumLengthOfStringAfterOperations_1(v[i])
        output.writelines(str(res1) + "\n")

        res2 = _03223_MinimumLengthOfStringAfterOperations_2(v[i])
        output.writelines(str(res2) + "\n")


# endregion


# region Problem Description
"""
You are given a string s.
You can perform the following process on s any number of times:
Choose an index i in the string such that there is at least one character to the left 
of index i that is equal to s[i], and at least one character to the right that is also 
equal to s[i].
Delete the closest character to the left of index i that is equal to s[i].
Delete the closest character to the right of index i that is equal to s[i].
Return the minimum length of the final string s that you can achieve.

Constraints:

1 <= s.length <= 2 * 10^5
s consists only of lowercase English letters.
"""


def _03223_MinimumLengthOfStringAfterOperations():
    os.system("cls")
    data_collector()
    solve()


_03223_MinimumLengthOfStringAfterOperations()
# endregion


# region Unit Testing
class _03223_MinimumLengthOfStringAfterOperations_Test(unittest.TestCase):
    def test_03223_MinimumLengthOfStringAfterOperations_0(self):
        for i in range(ncases):
            self.assertEqual(
                _03223_MinimumLengthOfStringAfterOperations_0(v[i]),
                v0[i],
            )

    def test_03223_MinimumLengthOfStringAfterOperations_1(self):
        for i in range(ncases):
            self.assertEqual(
                _03223_MinimumLengthOfStringAfterOperations_1(v[i]),
                v0[i],
            )

    def test_03223_MinimumLengthOfStringAfterOperations_2(self):
        for i in range(ncases):
            self.assertEqual(
                _03223_MinimumLengthOfStringAfterOperations_2(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
