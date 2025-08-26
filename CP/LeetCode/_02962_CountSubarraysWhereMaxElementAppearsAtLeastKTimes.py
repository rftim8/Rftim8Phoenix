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
        f"{cwd}/Data/CP/LeetCode/IO/_02962_CountSubarraysWhereMaxElementAppearsAtLeastKTimes_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02962_CountSubarraysWhereMaxElementAppearsAtLeastKTimes_Output.txt",
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
        v0.append(int(input[i + 1]))
        v1.append(int(input[i + 2]))


# endregion


# region Solutions
"""
"""


def _02962_CountSubarraysWhereMaxElementAppearsAtLeastKTimes_0(
    nums: List[int], k: int
) -> int:
    res = 0
    m = max(nums)
    l = 0
    c = 0
    for r in range(len(nums)):
        if nums[r] == m:
            c += 1
        while c == k:
            if nums[l] == m:
                c -= 1
            l += 1
        res += l

    return res


def solve():
    for i in range(ncases):
        res0 = _02962_CountSubarraysWhereMaxElementAppearsAtLeastKTimes_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
You are given an integer array nums and a positive integer k.
Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
A subarray is a contiguous sequence of elements within an array.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= k <= 10^5
"""


def _02962_CountSubarraysWhereMaxElementAppearsAtLeastKTimes():
    os.system("cls")
    data_collector()
    solve()


_02962_CountSubarraysWhereMaxElementAppearsAtLeastKTimes()
# endregion


# region Unit Testing
class _02962_CountSubarraysWhereMaxElementAppearsAtLeastKTimes_Test(unittest.TestCase):
    def test_02962_CountSubarraysWhereMaxElementAppearsAtLeastKTimes_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02962_CountSubarraysWhereMaxElementAppearsAtLeastKTimes_0(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
