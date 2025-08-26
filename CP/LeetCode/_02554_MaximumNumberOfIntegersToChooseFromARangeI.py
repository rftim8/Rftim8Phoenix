import os
from typing import List
import numpy as np
import timeit
import tracemalloc
import unittest
from os import path
import sys

os.system("cls")
cwd = os.getcwd()
sys.path.append(cwd)


# tracemalloc.start()

# region Data Gathering
with open(
    f"{cwd}/RftData/CP/LeetCode/IO/_02554_MaximumNumberOfIntegersToChooseFromARangeI_Input.txt"
) as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
# region Binary Search
def _custom_binary_search(arr: List[int], target: int) -> bool:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False


def _02554_MaximumNumberOfIntegersToChooseFromARangeI_0(
    banned: List[int], n: int, maxSum: int
) -> int:
    banned.sort()
    count = 0

    for num in range(1, n + 1):
        if _custom_binary_search(banned, num):
            continue

        maxSum -= num

        if maxSum < 0:
            break

        count += 1

    return count


# endregion


# region Sweep
def _02554_MaximumNumberOfIntegersToChooseFromARangeI_1(
    banned: List[int], n: int, maxSum: int
) -> int:
    banned.sort()
    banned_idx = 0
    count = 0

    for num in range(1, n + 1):
        if banned_idx < len(banned) and banned[banned_idx] == num:
            while banned_idx < len(banned) and banned[banned_idx] == num:
                banned_idx += 1
        else:
            maxSum -= num

            if maxSum >= 0:
                count += 1
            else:
                break

    return count


# endregion


# region Hash Set
def _02554_MaximumNumberOfIntegersToChooseFromARangeI_2(
    banned: List[int], n: int, maxSum: int
) -> int:
    banned_set = set(banned)
    count = 0

    for num in range(1, n + 1):
        if num in banned_set:
            continue

        if maxSum - num < 0:
            return count

        maxSum -= num
        count += 1

    return count


# endregion


# region Speed
def _02554_MaximumNumberOfIntegersToChooseFromARangeI_3(
    banned: List[int], n: int, maxSum: int
) -> int:
    ans = 0
    temp = 0
    banned = set(banned)

    for i in range(1, n + 1):
        if temp >= maxSum or temp + i > maxSum:
            break
        elif i not in banned:
            temp += i
            ans += 1

    return ans


# endregion

# tic = timeit.default_timer()
for i in range(2, (int(l[0]) * int(l[1])), int(l[1])):
    a = [int(i) for i in l[i].split(",")]
    b = int(l[i + 1])
    c = int(l[i + 2])
    print(
        f"_02554_MaximumNumberOfIntegersToChooseFromARangeI_0: {_02554_MaximumNumberOfIntegersToChooseFromARangeI_0(a,b,c)}"
    )
    print(
        f"_02554_MaximumNumberOfIntegersToChooseFromARangeI_1: {_02554_MaximumNumberOfIntegersToChooseFromARangeI_1(a,b,c)}"
    )
    print(
        f"_02554_MaximumNumberOfIntegersToChooseFromARangeI_2: {_02554_MaximumNumberOfIntegersToChooseFromARangeI_2(a,b,c)}"
    )
    print(
        f"_02554_MaximumNumberOfIntegersToChooseFromARangeI_3: {_02554_MaximumNumberOfIntegersToChooseFromARangeI_3(a,b,c)}"
    )
# snapshot1 = tracemalloc.take_snapshot()
# toc = timeit.default_timer()
# elapsed_time = toc - tic
# print(f"Execution time: {elapsed_time:.8f}s\n")
# endregion


# region Unit Testing
class _02554_MaximumNumberOfIntegersToChooseFromARangeI_Test(unittest.TestCase):
    with open(
        f"{cwd}/RftData/CP/LeetCode/IO/_02554_MaximumNumberOfIntegersToChooseFromARangeI_Input.txt"
    ) as input:
        l = input.read().strip().splitlines()

        def test_02554_MaximumNumberOfIntegersToChooseFromARangeI(self):
            for i in range(2, (int(l[0]) * int(l[1])), int(l[1])):
                a = [int(i) for i in l[i].split(",")]
                b = int(l[i + 1])
                c = int(l[i + 2])
                d = int(l[i + 3])

                self.assertEqual(
                    _02554_MaximumNumberOfIntegersToChooseFromARangeI_0(a, b, c), d
                )

                self.assertEqual(
                    _02554_MaximumNumberOfIntegersToChooseFromARangeI_1(a, b, c), d
                )

                self.assertEqual(
                    _02554_MaximumNumberOfIntegersToChooseFromARangeI_2(a, b, c), d
                )

                self.assertEqual(
                    _02554_MaximumNumberOfIntegersToChooseFromARangeI_3(a, b, c), d
                )


unittest.main(argv=[""], verbosity=1, exit=False)

# region Memory Profiling
# top_stats = snapshot1.statistics("lineno")
# for i in top_stats:
#     print(i)
# endregion
