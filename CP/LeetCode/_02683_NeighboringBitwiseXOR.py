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
    open(f"{cwd}/Data/CP/LeetCode/IO/_02683_NeighboringBitwiseXOR_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_02683_NeighboringBitwiseXOR_Output.txt", "w")


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(rft_stl.string_to_1D_list_of_int(input[i]))
        v0.append(True if input[i + 1] == "true" else False)


# endregion


# region Solutions
"""
Simulation
"""


def _02683_NeighboringBitwiseXOR_0(derived: List[int]) -> bool:
    original = [0]
    for i in range(len(derived)):
        original.append(derived[i] ^ original[i])

    check_for_zero = original[0] == original[-1]
    original = [1]
    for i in range(len(derived)):
        original.append(derived[i] ^ original[i])
    check_for_one = original[0] == original[-1]

    return check_for_zero or check_for_one


"""
Cumulative XOR
"""


def _02683_NeighboringBitwiseXOR_1(derived: List[int]) -> bool:
    return sum(derived) % 2 == 0


"""
Sum Parity
"""


def _02683_NeighboringBitwiseXOR_2(derived: List[int]) -> bool:
    XOR = 0
    for element in derived:
        XOR = XOR ^ element

    return XOR == 0


def solve():
    for i in range(ncases):
        res0 = _02683_NeighboringBitwiseXOR_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _02683_NeighboringBitwiseXOR_1(v[i])
        output.writelines(str(res1) + "\n")

        res2 = _02683_NeighboringBitwiseXOR_2(v[i])
        output.writelines(str(res2) + "\n")


# endregion


# region Problem Description
"""
A 0-indexed array derived with length n is derived by computing the bitwise XOR (⊕) 
of adjacent values in a binary array original of length n.
Specifically, for each index i in the range [0, n - 1]:
If i = n - 1, then derived[i] = original[i] ⊕ original[0].
Otherwise, derived[i] = original[i] ⊕ original[i + 1].
Given an array derived, your task is to determine whether there exists a valid binary 
array original that could have formed derived.
Return true if such an array exists or false otherwise.
A binary array is an array containing only 0's and 1's
Constraints:

n == derived.length
1 <= n <= 105
The values in derived are either 0's or 1's
"""


def _02683_NeighboringBitwiseXOR():
    os.system("cls")
    data_collector()
    solve()


_02683_NeighboringBitwiseXOR()
# endregion


# region Unit Testing
class _02683_NeighboringBitwiseXOR_Test(unittest.TestCase):
    def test_02683_NeighboringBitwiseXOR_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02683_NeighboringBitwiseXOR_0(v[i]),
                v0[i],
            )

    def test_02683_NeighboringBitwiseXOR_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02683_NeighboringBitwiseXOR_1(v[i]),
                v0[i],
            )

    def test_02683_NeighboringBitwiseXOR_2(self):
        for i in range(ncases):
            self.assertEqual(
                _02683_NeighboringBitwiseXOR_2(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
