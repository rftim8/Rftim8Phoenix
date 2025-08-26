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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_05_PrintQueue_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0
    a = False
    b = []
    c = []

    for i in l:
        if i == "":
            a = True
        elif a:
            c.append(i)
        else:
            b.append(i)

    for i in c:
        e = True
        d = i.split(",")
        for j in range(len(d)):
            for k in range(j + 1, len(d)):
                for m in b:
                    x = m.split("|")[0]
                    y = m.split("|")[1]
                    if d[j] == y and d[k] == x:
                        e = False
        if e:
            f = int(len(d) / 2)
            res += int(d[f])

    return res


def part_two() -> int:
    res = 0
    a = False
    b = []
    c = []

    for i in l:
        if i == "":
            a = True
        elif a:
            c.append(i)
        else:
            b.append(i)

    for i in c:
        e = True
        d = i.split(",")
        for j in range(len(d)):
            for k in range(j + 1, len(d)):
                for m in b:
                    x = m.split("|")[0]
                    y = m.split("|")[1]
                    if d[j] == y and d[k] == x:
                        d[j] = x
                        d[k] = y
                        e = False
        if not e:
            f = int(len(d) / 2)
            res += int(d[f])

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
class _05_PrintQueue_Test(unittest.TestCase):
    with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_05_PrintQueue_Output.txt") as input:
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
