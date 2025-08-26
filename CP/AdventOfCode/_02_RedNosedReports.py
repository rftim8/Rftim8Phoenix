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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_02_RedNosedReports_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0

    for i in l:
        a = [int(j) for j in i.split()]
        b = []

        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                b.append(1)
            elif a[j] < a[j + 1]:
                b.append(0)
            else:
                b.append(2)

        if b.count(0) == len(a) - 1 or b.count(1) == len(a) - 1:
            c = 0
            for j in range(len(a) - 1):
                if 0 < abs(a[j] - a[j + 1]) < 4:
                    c += 1

            if c == len(a) - 1:
                res += 1

    return res


def part_two() -> int:
    res = 0

    for i in l:
        a = list(map(int, i.split()))
        b = False

        for j in range(len(a)):
            l0 = a[:j] + a[j + 1 :]
            dir = l0 == sorted(l0) or l0 == sorted(l0, reverse=True)
            d = True

            for i in range(len(l0) - 1):
                diff = abs(l0[i] - l0[i + 1])

                if not 1 <= diff <= 3:
                    d = False
                    continue

            if dir and d:
                b = True

        if b:
            res += 1

    return res


# tic = timeit.default_timer()
print(f"Part One: {part_one()}")
# snapshot1 = tracemalloc.take_snapshot()
# toc = timeit.default_timer()
# elapsed_time = toc - tic
# print(f"Execution time: {elapsed_time:.8f}s\n")

# tic = timeit.default_timer()
print(f"Part Two: {part_two()}")
# snapshot1 = tracemalloc.take_snapshot()
# toc = timeit.default_timer()
# elapsed_time = toc - tic
# print(f"Execution time: {elapsed_time:.8f}s")
# endregion


# region Unit Testing
class _02_RedNosedReports_Test(unittest.TestCase):
    with open(
        f"{cwd}/RftData/CP/AdventOfCode/IO/_02_RedNosedReports_Output.txt"
    ) as input:
        l = input.read().strip().splitlines()

    def test_part_one(self):
        self.assertEqual(part_one(), int(self.l[0]))

    def test_part_two(self):
        self.assertEqual(part_two(), int(self.l[1]))


unittest.main(argv=[""], verbosity=1, exit=False)

# region Memory Profiling
# top_stats = snapshot1.statistics("lineno")
# for i in top_stats:
#     print(i)
# endregion
