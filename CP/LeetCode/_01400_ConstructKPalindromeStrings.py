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
    open(f"{cwd}/Data/CP/LeetCode/IO/_01400_ConstructKPalindromeStrings_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_01400_ConstructKPalindromeStrings_Output.txt", "w"
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
        v0.append(int(input[i + 1]))
        v1.append(True if input[i + 2] == "true" else False)


# endregion


# region Solutions
"""
"""


def _01400_ConstructKPalindromeStrings_0(s: str, k: int) -> bool:
    if len(s) < k:
        return False

    b = {}
    for i in s:
        b[i] = b.get(i, 0) + 1

    c = 0
    for i in b.values():
        if i % 2 != 0:
            c += 1

    if c > k:
        return False

    return True


"""
Optimized
"""


def _01400_ConstructKPalindromeStrings_1(s: str, k: int) -> bool:
    if len(s) == k:
        return True
    if len(s) < k:
        return False
    odd = 0
    for char in set(s):
        if s.count(char) % 2:
            odd += 1
    if odd > k:
        return False
    return True


"""
Bit Manipulation
"""


def _01400_ConstructKPalindromeStrings_2(s: str, k: int) -> bool:
    if len(s) < k:
        return False

    if len(s) == k:
        return True

    odd_count = 0

    for chr in s:
        odd_count ^= 1 << (ord(chr) - ord("a"))

    return bin(odd_count).count("1") <= k


def solve():
    for i in range(ncases):
        res0 = _01400_ConstructKPalindromeStrings_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")

        res1 = _01400_ConstructKPalindromeStrings_1(v[i], v0[i])
        output.writelines(str(res1) + "\n")

        res2 = _01400_ConstructKPalindromeStrings_2(v[i], v0[i])
        output.writelines(str(res2) + "\n")


# endregion


# region Problem Description
"""
Given a string s and an integer k, return true if you can use all the characters in s to construct 
k palindrome strings or false otherwise.

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= 10^5
"""


def _01400_ConstructKPalindromeStrings():
    os.system("cls")
    data_collector()
    solve()


_01400_ConstructKPalindromeStrings()
# endregion


# region Unit Testing
class _01400_ConstructKPalindromeStrings_Test(unittest.TestCase):
    def test_01400_ConstructKPalindromeStrings_0(self):
        for i in range(ncases):
            self.assertEqual(
                _01400_ConstructKPalindromeStrings_0(v[i], v0[i]),
                v1[i],
            )

    def test_01400_ConstructKPalindromeStrings_1(self):
        for i in range(ncases):
            self.assertEqual(
                _01400_ConstructKPalindromeStrings_1(v[i], v0[i]),
                v1[i],
            )

    def test_01400_ConstructKPalindromeStrings_2(self):
        for i in range(ncases):
            self.assertEqual(
                _01400_ConstructKPalindromeStrings_2(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
