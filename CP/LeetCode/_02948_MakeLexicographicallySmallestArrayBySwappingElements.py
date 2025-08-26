# region Imports
from collections import deque
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
        f"{cwd}/Data/CP/LeetCode/IO/_02948_MakeLexicographicallySmallestArrayBySwappingElements_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02948_MakeLexicographicallySmallestArrayBySwappingElements_Output.txt",
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
        v1.append(rft_stl.string_to_1D_list_of_int(input[i + 2]))


# endregion


# region Solutions
"""
Sorting + Grouping
"""


def _02948_MakeLexicographicallySmallestArrayBySwappingElements_0(
    nums: List[int], limit: int
) -> List[int]:
    nums_sorted = sorted(nums)
    curr_group = 0
    num_to_group = {}
    num_to_group[nums_sorted[0]] = curr_group

    group_to_list = {}
    group_to_list[curr_group] = deque([nums_sorted[0]])

    for i in range(1, len(nums)):
        if abs(nums_sorted[i] - nums_sorted[i - 1]) > limit:
            curr_group += 1

        num_to_group[nums_sorted[i]] = curr_group

        if curr_group not in group_to_list:
            group_to_list[curr_group] = deque()

        group_to_list[curr_group].append(nums_sorted[i])

    for i in range(len(nums)):
        num = nums[i]
        group = num_to_group[num]
        nums[i] = group_to_list[group].popleft()

    return nums


"""
Speed
"""


def _02948_MakeLexicographicallySmallestArrayBySwappingElements_1(
    nums: List[int], limit: int
) -> List[int]:
    n = len(nums)
    ordered_nums = sorted(nums)
    prev = ordered_nums[0]
    num_to_group = {}
    current_group = 0
    group_start = [0]

    for i, x in enumerate(ordered_nums):
        if x - prev > limit:
            current_group += 1
            group_start.append(i)

        num_to_group[x] = current_group
        prev = x

    result = []
    for x in nums:
        group = num_to_group[x]
        result.append(ordered_nums[group_start[group]])
        group_start[group] += 1

    return result


def solve():
    for i in range(ncases):
        res0 = _02948_MakeLexicographicallySmallestArrayBySwappingElements_0(
            v[i], v0[i]
        )
        for j in res0:
            output.write(str(j) + " ")
        output.write("\n")

        res1 = _02948_MakeLexicographicallySmallestArrayBySwappingElements_1(
            v[i], v0[i]
        )
        for j in res1:
            output.write(str(j) + " ")
        output.write("\n")


# endregion


# region Problem Description
"""
You are given a 0-indexed array of positive integers nums and a positive integer limit.
In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if 
|nums[i] - nums[j]| <= limit.
Return the lexicographically smallest array that can be obtained by performing 
the operation any number of times.
An array a is lexicographically smaller than an array b if in the first position 
where a and b differ, array a has an element that is less than the corresponding 
element in b. 
For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] 
because they differ at index 0 and 2 < 10.
Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= limit <= 10^9
"""


def _02948_MakeLexicographicallySmallestArrayBySwappingElements():
    os.system("cls")
    data_collector()
    solve()


_02948_MakeLexicographicallySmallestArrayBySwappingElements()
# endregion


# region Unit Testing
class _02948_MakeLexicographicallySmallestArrayBySwappingElements_Test(
    unittest.TestCase
):
    def test_02948_MakeLexicographicallySmallestArrayBySwappingElements_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02948_MakeLexicographicallySmallestArrayBySwappingElements_0(
                    v[i], v0[i]
                ),
                v1[i],
            )

    def test_02948_MakeLexicographicallySmallestArrayBySwappingElements_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02948_MakeLexicographicallySmallestArrayBySwappingElements_1(
                    v[i], v0[i]
                ),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
