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
        f"{cwd}/Data/CP/LeetCode/IO/_03396_MinimumNumberOfOperationsToMakeElementsInArrayDistinct_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_03396_MinimumNumberOfOperationsToMakeElementsInArrayDistinct_Output.txt",
    "w",
)


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(rft_stl.string_to_1D_list_of_int(input[i]))
        v0.append(int(input[i + 1]))


# endregion


# region Solutions
"""
Set
"""


def _03396_MinimumNumberOfOperationsToMakeElementsInArrayDistinct_0(
    nums: List[int],
) -> int:
    res = 0
    for i in range(0, len(nums), 3):
        if len(nums[i:]) != len(set(nums[i:])):
            res += 1

    return res


"""
Speed
"""


def _03396_MinimumNumberOfOperationsToMakeElementsInArrayDistinct_1(
    nums: List[int],
) -> int:
    n = len(nums)
    m = {}
    mark = -1

    for i in range(n - 1, -1, -1):
        if nums[i] not in m:
            m[nums[i]] = 1
        else:
            mark = i
            break

    if mark == -1:
        return 0
    elif n <= 3 and mark != -1:
        return 1
    elif (mark + 1) % 3 == 0:
        return (mark + 1) // 3

    return ((mark + 1) // 3) + 1


def solve():
    for i in range(ncases):
        res0 = _03396_MinimumNumberOfOperationsToMakeElementsInArrayDistinct_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _03396_MinimumNumberOfOperationsToMakeElementsInArrayDistinct_1(v[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
You are given an integer array nums. 
You need to ensure that the elements in the array are distinct. 
To achieve this, you can perform the following operation any number of times:
Remove 3 elements from the beginning of the array. 
If the array has fewer than 3 elements, remove all remaining elements.
Note that an empty array is considered to have distinct elements. 
Return the minimum number of operations needed to make the elements in the array distinct.

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""


def _03396_MinimumNumberOfOperationsToMakeElementsInArrayDistinct():
    os.system("cls")
    data_collector()
    solve()


_03396_MinimumNumberOfOperationsToMakeElementsInArrayDistinct()
# endregion


# region Unit Testing
class _03396_MinimumNumberOfOperationsToMakeElementsInArrayDistinct_Test(
    unittest.TestCase
):
    def test_03396_MinimumNumberOfOperationsToMakeElementsInArrayDistinct_0(self):
        for i in range(ncases):
            self.assertEqual(
                _03396_MinimumNumberOfOperationsToMakeElementsInArrayDistinct_0(v[i]),
                v0[i],
            )

    def test_03396_MinimumNumberOfOperationsToMakeElementsInArrayDistinct_1(self):
        for i in range(ncases):
            self.assertEqual(
                _03396_MinimumNumberOfOperationsToMakeElementsInArrayDistinct_1(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
