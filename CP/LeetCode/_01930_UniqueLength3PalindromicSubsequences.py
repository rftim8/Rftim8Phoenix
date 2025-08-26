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
        f"{cwd}/Data/CP/LeetCode/IO/_01930_UniqueLength3PalindromicSubsequences_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_01930_UniqueLength3PalindromicSubsequences_Output.txt",
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
Count Letters In-Between
"""


def _01930_UniqueLength3PalindromicSubsequences_0(s: str) -> int:
    res = 0
    letters = set(s)

    for letter in letters:
        i = -1
        j = 0

        for k in range(len(s)):
            if s[k] == letter:
                if i == -1:
                    i = k
                j = k

        between = set()

        for k in range(i + 1, j):
            between.add(s[k])

        res += len(between)

    return res


def solve():
    for i in range(ncases):
        res0 = _01930_UniqueLength3PalindromicSubsequences_0(v[i])
        output.writelines(str(res0) + "\n")


"""
Pre-Compute First And Last Indices
"""


def _01930_UniqueLength3PalindromicSubsequences_1(s: str) -> int:
    first = [-1] * 26
    last = [-1] * 26

    for i in range(len(s)):
        curr = ord(s[i]) - ord("a")
        if first[curr] == -1:
            first[curr] = i

        last[curr] = i

    ans = 0
    for i in range(26):
        if first[i] == -1:
            continue

        between = set()
        for j in range(first[i] + 1, last[i]):
            between.add(s[j])

        ans += len(between)

    return ans


def solve():
    for i in range(ncases):
        res0 = _01930_UniqueLength3PalindromicSubsequences_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _01930_UniqueLength3PalindromicSubsequences_1(v[i])
        output.writelines(str(res1) + "\n")


"""
Speed
"""


def _01930_UniqueLength3PalindromicSubsequences_2(s: str) -> int:
    c = "abcdefghijklmnopqrstuvwxyz"
    a, t = 0, 0

    for x in c:
        l = s.find(x)
        if l == -1:
            continue
        r = s.rfind(x)
        if l >= r:
            continue

        v = [False] * 128
        t = 0
        for i in range(l + 1, r):
            if not v[ord(s[i])]:
                v[ord(s[i])] = True
                t += 1
                if t == 26:
                    break
        a += t
    return a


def solve():
    for i in range(ncases):
        res0 = _01930_UniqueLength3PalindromicSubsequences_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _01930_UniqueLength3PalindromicSubsequences_1(v[i])
        output.writelines(str(res1) + "\n")

        res2 = _01930_UniqueLength3PalindromicSubsequences_2(v[i])
        output.writelines(str(res2) + "\n")


# endregion


# region Problem Description
"""
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
A palindrome is a string that reads the same forwards and backwards.
A subsequence of a string is a new string generated from the original string with some characters 
(can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".

Constraints:

3 <= s.length <= 10^5
s consists of only lowercase English letters.
"""


def _01930_UniqueLength3PalindromicSubsequences():
    os.system("cls")
    data_collector()
    solve()


_01930_UniqueLength3PalindromicSubsequences()
# endregion


# region Unit Testing
class _01930_UniqueLength3PalindromicSubsequences_Test(unittest.TestCase):
    def test_01930_UniqueLength3PalindromicSubsequences_0(self):
        for i in range(ncases):
            self.assertEqual(
                _01930_UniqueLength3PalindromicSubsequences_0(v[i]),
                v0[i],
            )

    def test_01930_UniqueLength3PalindromicSubsequences_1(self):
        for i in range(ncases):
            self.assertEqual(
                _01930_UniqueLength3PalindromicSubsequences_1(v[i]),
                v0[i],
            )

    def test_01930_UniqueLength3PalindromicSubsequences_2(self):
        for i in range(ncases):
            self.assertEqual(
                _01930_UniqueLength3PalindromicSubsequences_2(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
