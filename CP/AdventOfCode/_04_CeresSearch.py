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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_04_CeresSearch_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0

    x = len(l[0])
    y = len(l)

    a = ""
    for i in range(x + 6):
        a += "."

    for i in range(y):
        l[i] = f"...{l[i]}..."

    l.insert(0, a)
    l.insert(0, a)
    l.insert(0, a)
    l.append(a)
    l.append(a)
    l.append(a)

    for i in range(3, y + 3):
        for j in range(3, x + 3):
            # south
            if (
                l[i][j] == "X"
                and l[i + 1][j] == "M"
                and l[i + 2][j] == "A"
                and l[i + 3][j] == "S"
            ):
                res += 1
            # north
            if (
                l[i][j] == "X"
                and l[i - 1][j] == "M"
                and l[i - 2][j] == "A"
                and l[i - 3][j] == "S"
            ):
                res += 1
            # east
            if (
                l[i][j] == "X"
                and l[i][j + 1] == "M"
                and l[i][j + 2] == "A"
                and l[i][j + 3] == "S"
            ):
                res += 1
            # west
            if (
                l[i][j] == "X"
                and l[i][j - 1] == "M"
                and l[i][j - 2] == "A"
                and l[i][j - 3] == "S"
            ):
                res += 1
            # south east
            if (
                l[i][j] == "X"
                and l[i + 1][j + 1] == "M"
                and l[i + 2][j + 2] == "A"
                and l[i + 3][j + 3] == "S"
            ):
                res += 1
            # north west
            if (
                l[i][j] == "X"
                and l[i - 1][j - 1] == "M"
                and l[i - 2][j - 2] == "A"
                and l[i - 3][j - 3] == "S"
            ):
                res += 1
            # north east
            if (
                l[i][j] == "X"
                and l[i - 1][j + 1] == "M"
                and l[i - 2][j + 2] == "A"
                and l[i - 3][j + 3] == "S"
            ):
                res += 1
            # south west
            if (
                l[i][j] == "X"
                and l[i + 1][j - 1] == "M"
                and l[i + 2][j - 2] == "A"
                and l[i + 3][j - 3] == "S"
            ):
                res += 1

    return res


def part_two() -> int:
    res = 0

    x = len(l[0])
    y = len(l)

    a = ""
    for i in range(x + 6):
        a += "."

    for i in range(y):
        l[i] = f"...{l[i]}..."

    l.insert(0, a)
    l.insert(0, a)
    l.insert(0, a)
    l.append(a)
    l.append(a)
    l.append(a)

    for i in range(3, y + 3):
        for j in range(3, x + 3):
            # south
            if (
                (
                    l[i][j] == "A"
                    and l[i + 1][j + 1] == "M"
                    and l[i - 1][j - 1] == "S"
                    and l[i + 1][j - 1] == "M"
                    and l[i - 1][j + 1] == "S"
                )
                or (
                    l[i][j] == "A"
                    and l[i + 1][j + 1] == "S"
                    and l[i - 1][j - 1] == "M"
                    and l[i + 1][j - 1] == "M"
                    and l[i - 1][j + 1] == "S"
                )
                or (
                    l[i][j] == "A"
                    and l[i + 1][j + 1] == "S"
                    and l[i - 1][j - 1] == "M"
                    and l[i + 1][j - 1] == "S"
                    and l[i - 1][j + 1] == "M"
                )
                or (
                    l[i][j] == "A"
                    and l[i + 1][j + 1] == "M"
                    and l[i - 1][j - 1] == "S"
                    and l[i + 1][j - 1] == "S"
                    and l[i - 1][j + 1] == "M"
                )
            ):
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
class _04_CeresSearch_Test(unittest.TestCase):
    with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_04_CeresSearch_Output.txt") as input:
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
