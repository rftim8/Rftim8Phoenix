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
    open(f"{cwd}/Data/CP/LeetCode/IO/_02429_MinimizeXOR_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_02429_MinimizeXOR_Output.txt", "w")


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []
v1 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(int(input[i]))
        v0.append(int(input[i + 1]))
        v1.append(int(input[i + 2]))


# endregion


# region Solutions
"""
From optimal to valid
"""


def _is_set(x: int, bit: int) -> bool:
    return (x & (1 << bit)) != 0


def _set_bit(x: int, bit: int):
    return x | (1 << bit)


def _unset_bit(x: int, bit: int):
    return x & ~(1 << bit)


def _02429_MinimizeXOR_0(num1: int, num2: int) -> int:
    result = num1
    target_set_bits_count = bin(num2).count("1")
    set_bits_count = bin(result).count("1")
    current_bit = 0

    while set_bits_count < target_set_bits_count:
        if not _is_set(result, current_bit):
            result = _set_bit(result, current_bit)
            set_bits_count += 1
        current_bit += 1

    while set_bits_count > target_set_bits_count:
        if _is_set(result, current_bit):
            result = _unset_bit(result, current_bit)
            set_bits_count -= 1
        current_bit += 1

    return result


"""
Building the answer
"""


def _02429_MinimizeXOR_1(num1: int, num2: int) -> int:
    result = 0
    target_set_bits_count = bin(num2).count("1")
    set_bits_count = 0
    current_bit = 31

    while set_bits_count < target_set_bits_count:
        if _is_set(num1, current_bit) or (
            target_set_bits_count - set_bits_count > current_bit
        ):
            result = _set_bit(result, current_bit)
            set_bits_count += 1
        current_bit -= 1

    return result


"""
Speed
"""


def _02429_MinimizeXOR_2(num1: int, num2: int) -> int:
    bits1 = bin(num1).count("1")
    bits2 = bin(num2).count("1")

    if bits1 == bits2:
        return num1

    if bits1 > bits2:
        r = num1
        remove = bits1 - bits2
        x = 1
        while remove > 0:
            if r & x > 0:
                r ^= x
                remove -= 1
            x <<= 1
        return r

    if bits1 < bits2:
        r = num1
        add = bits2 - bits1
        x = 1
        while add > 0:
            if r & x == 0:
                r |= x
                add -= 1
            x <<= 1
        return r


def solve():
    for i in range(ncases):
        res0 = _02429_MinimizeXOR_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")

        res1 = _02429_MinimizeXOR_1(v[i], v0[i])
        output.writelines(str(res1) + "\n")

        res2 = _02429_MinimizeXOR_2(v[i], v0[i])
        output.writelines(str(res2) + "\n")


# endregion


# region Problem Description
"""
Given two positive integers num1 and num2, find the positive integer x such that:
x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.
Return the integer x. The test cases are generated such that x is uniquely determined.
The number of set bits of an integer is the number of 1's in its binary representation.

Constraints:

1 <= num1, num2 <= 10^9
"""


def _02429_MinimizeXOR():
    os.system("cls")
    data_collector()
    solve()


_02429_MinimizeXOR()
# endregion


# region Unit Testing
class _02429_MinimizeXOR_Test(unittest.TestCase):
    def test_02429_MinimizeXOR_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02429_MinimizeXOR_0(v[i], v0[i]),
                v1[i],
            )

    def test_02429_MinimizeXOR_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02429_MinimizeXOR_1(v[i], v0[i]),
                v1[i],
            )

    def test_02429_MinimizeXOR_2(self):
        for i in range(ncases):
            self.assertEqual(
                _02429_MinimizeXOR_2(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
