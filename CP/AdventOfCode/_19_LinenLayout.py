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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_19_LinenLayout_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0

    towels = []
    designs = []

    g = list(l)
    f = True

    for i in g:
        if i == "":
            f = False
        else:
            if f:
                towels = i.split(", ")
            else:
                designs.append(i)

    DP = {}

    def com(towels, design):
        if design in DP:
            return DP[design]
        res = False
        if not design:
            res = True
        for towel in towels:
            if design.startswith(towel) and com(towels, design[len(towel) :]):
                res = True
        DP[design] = res
        return res

    for design in designs:
        if com(towels, design):
            res += 1

    return res


def part_two() -> int:
    res = 0

    towels = []
    designs = []

    g = list(l)
    f = True

    for i in g:
        if i == "":
            f = False
        else:
            if f:
                towels = i.split(", ")
            else:
                designs.append(i)

    DP = {}

    def com(towels, design):
        if design in DP:
            return DP[design]
        res = 0
        if not design:
            res = 1
        for towel in towels:
            if design.startswith(towel):
                res += com(towels, design[len(towel) :])
        DP[design] = res
        return res

    for design in designs:
        res += com(towels, design)

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
class _19_LinenLayout_Test(unittest.TestCase):
    with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_19_LinenLayout_Output.txt") as input:
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
