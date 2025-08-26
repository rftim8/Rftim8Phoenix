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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_13_ClawContraption_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0

    a = list(l)
    c = 100

    for i in range(0, len(a), 4):
        ax = int(a[i].split(":")[1].split(",")[0].split("+")[1])
        ay = int(a[i].split(":")[1].split(",")[1].split("+")[1])
        bx = int(a[i + 1].split(":")[1].split(",")[0].split("+")[1])
        by = int(a[i + 1].split(":")[1].split(",")[1].split("+")[1])
        sx = int(a[i + 2].split(":")[1].split(",")[0].split("=")[1])
        sy = int(a[i + 2].split(":")[1].split(",")[1].split("=")[1])

        f = sys.maxsize
        for j in range(c):
            for k in range(c):
                if j * ax + k * bx == sx and j * ay + k * by == sy:
                    if j * 3 + k < f:
                        f = j * 3 + k
                    # r.append((ax, ay, bx, by, j * 3 + k))

        # sorted(r, reverse=True)
        # print(r)
        # print(f)
        if f != sys.maxsize:
            res += f

    return res


def part_two() -> int:
    res = 0

    a = list(l)

    for i in range(0, len(a), 4):
        ax = int(a[i].split(":")[1].split(",")[0].split("+")[1])
        ay = int(a[i].split(":")[1].split(",")[1].split("+")[1])
        bx = int(a[i + 1].split(":")[1].split(",")[0].split("+")[1])
        by = int(a[i + 1].split(":")[1].split(",")[1].split("+")[1])
        sx = int(a[i + 2].split(":")[1].split(",")[0].split("=")[1]) + 10000000000000
        sy = int(a[i + 2].split(":")[1].split(",")[1].split("=")[1]) + 10000000000000

        x = round((sy - ((by * sx) / bx)) / (ay - ((by * ax) / bx)))
        y = round((sx - ax * x) / bx)

        if ax * x + bx * y == sx and ay * x + by * y == sy:
            res += x * 3 + y

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
class _13_ClawContraption_Test(unittest.TestCase):
    with open(
        f"{cwd}/RftData/CP/AdventOfCode/IO/_13_ClawContraption_Output.txt"
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
