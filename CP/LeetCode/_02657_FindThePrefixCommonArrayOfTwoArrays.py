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
        f"{cwd}/Data/CP/LeetCode/IO/_02657_FindThePrefixCommonArrayOfTwoArrays_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02657_FindThePrefixCommonArrayOfTwoArrays_Output.txt",
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
        v0.append(rft_stl.string_to_1D_list_of_int(input[i + 1]))
        v1.append(rft_stl.string_to_1D_list_of_int(input[i + 2]))


# endregion


# region Solutions
"""
Brute Force
"""


def _02657_FindThePrefixCommonArrayOfTwoArrays_0(
    A: List[int], B: List[int]
) -> List[int]:
    n = len(A)
    res = []
    a = set()
    b = set()

    for i in range(n):
        s = 0
        a.add(A[i])
        b.add(B[i])
        for j in b:
            if j in a:
                s += 1
        res.append(s)

    return res


"""
Speed
"""


def _02657_FindThePrefixCommonArrayOfTwoArrays_1(
    A: List[int], B: List[int]
) -> List[int]:
    n = len(A)
    C = [0] * n
    seta, setb = set(), set()

    for i in range(n):
        C[i] = C[i - 1]
        if A[i] == B[i]:
            C[i] += 1
        else:
            if A[i] in setb:
                C[i] += 1
            if B[i] in seta:
                C[i] += 1
            seta.add(A[i])
            setb.add(B[i])

    return C


def solve():
    for i in range(ncases):
        res0 = _02657_FindThePrefixCommonArrayOfTwoArrays_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")

        res1 = _02657_FindThePrefixCommonArrayOfTwoArrays_1(v[i], v0[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
You are given two 0-indexed integer permutations A and B of length n.
A prefix common array of A and B is an array C such that C[i] is equal to the count 
of numbers that are present at or before the index i in both A and B.
Return the prefix common array of A and B.
A sequence of n integers is called a permutation if it contains all integers from 1 to n 
exactly once.

Constraints:

1 <= A.length == B.length == n <= 50
1 <= A[i], B[i] <= n
It is guaranteed that A and B are both a permutation of n integers.
"""


def _02657_FindThePrefixCommonArrayOfTwoArrays():
    os.system("cls")
    data_collector()
    solve()


_02657_FindThePrefixCommonArrayOfTwoArrays()
# endregion


# region Unit Testing
class _02657_FindThePrefixCommonArrayOfTwoArrays_Test(unittest.TestCase):
    def test_02657_FindThePrefixCommonArrayOfTwoArrays_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02657_FindThePrefixCommonArrayOfTwoArrays_0(v[i], v0[i]),
                v1[i],
            )

    def test_02657_FindThePrefixCommonArrayOfTwoArrays_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02657_FindThePrefixCommonArrayOfTwoArrays_1(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
