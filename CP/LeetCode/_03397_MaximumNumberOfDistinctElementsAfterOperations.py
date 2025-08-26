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
        f"{cwd}/Data/CP/LeetCode/IO/_03397_MaximumNumberOfDistinctElementsAfterOperations_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_03397_MaximumNumberOfDistinctElementsAfterOperations_Output.txt",
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


def _03397_MaximumNumberOfDistinctElementsAfterOperations_0(
    nums: List[int], k: int
) -> int:
    res = 0

    return res


def solve():
    for i in range(ncases):
        res0 = _03397_MaximumNumberOfDistinctElementsAfterOperations_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
You are given an integer array nums and an integer k.
You are allowed to perform the following operation on each element of the array at most once:
Add an integer in the range [-k, k] to the element.
Return the maximum possible number of distinct elements in nums after performing the operations.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= k <= 10^9
"""


def _03397_MaximumNumberOfDistinctElementsAfterOperations():
    os.system("cls")
    data_collector()
    solve()


_03397_MaximumNumberOfDistinctElementsAfterOperations()
# endregion


# region Unit Testing
class _03397_MaximumNumberOfDistinctElementsAfterOperations_Test(unittest.TestCase):
    def test_03397_MaximumNumberOfDistinctElementsAfterOperations_0(self):
        for i in range(ncases):
            self.assertEqual(
                _03397_MaximumNumberOfDistinctElementsAfterOperations_0(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
