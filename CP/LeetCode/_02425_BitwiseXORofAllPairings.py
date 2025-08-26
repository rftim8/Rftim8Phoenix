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
    open(f"{cwd}/Data/CP/LeetCode/IO/_02425_BitwiseXORofAllPairings_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02425_BitwiseXORofAllPairings_Output.txt", "w"
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
        v1.append(int(input[i + 2]))


# endregion


# region Solutions
"""
Hash Map
"""


def _02425_BitwiseXORofAllPairings_0(nums1: List[int], nums2: List[int]) -> int:
    len1, len2 = len(nums1), len(nums2)
    freq = {}

    for num in nums1:
        freq[num] = freq.get(num, 0) + len2

    for num in nums2:
        freq[num] = freq.get(num, 0) + len1

    ans = 0

    for num in freq:
        if freq[num] % 2:
            ans ^= num

    return ans


"""
Space Optimized Bit Manipulation
"""


def _02425_BitwiseXORofAllPairings_1(nums1: List[int], nums2: List[int]) -> int:
    xor1, xor2 = 0, 0
    len1, len2 = len(nums1), len(nums2)

    if len2 % 2:
        for num in nums1:
            xor1 ^= num

    if len1 % 2:
        for num in nums2:
            xor2 ^= num

    return xor1 ^ xor2


def solve():
    for i in range(ncases):
        res0 = _02425_BitwiseXORofAllPairings_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")

        res1 = _02425_BitwiseXORofAllPairings_1(v[i], v0[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. 
There exists another array, nums3, which contains the bitwise XOR of all pairings of integers 
between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).
Return the bitwise XOR of all integers in nums3.

Constraints:

1 <= nums1.length, nums2.length <= 10^5
0 <= nums1[i], nums2[j] <= 10^9
"""


def _02425_BitwiseXORofAllPairings():
    os.system("cls")
    data_collector()
    solve()


_02425_BitwiseXORofAllPairings()
# endregion


# region Unit Testing
class _02425_BitwiseXORofAllPairings_Test(unittest.TestCase):
    def test_02425_BitwiseXORofAllPairings_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02425_BitwiseXORofAllPairings_0(v[i], v0[i]),
                v1[i],
            )

    def test_02425_BitwiseXORofAllPairings_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02425_BitwiseXORofAllPairings_1(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
