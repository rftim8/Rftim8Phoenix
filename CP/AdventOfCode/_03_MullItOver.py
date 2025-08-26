import os
from typing import List
import numpy as np
import timeit
import tracemalloc
import unittest
from os import path
import sys
import re

os.system("cls")
cwd = os.getcwd()
sys.path.append(cwd)


# tracemalloc.start()

# region Data Gathering
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_03_MullItOver_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0

    for i in l:
        x = re.findall(r"mul\(\d+,\d+\)", i)

        for j in x:
            a = j.replace("mul(", "").replace(")", "")
            res += int(a.split(",")[0]) * int(a.split(",")[1])

    return res


def part_two() -> int:
    res = 0

    q = ""
    for i in l:
        q += i

    l0 = []

    x = re.findall(r"mul\(\d+,\d+\)", q)
    y = [i.start(0) for i in re.finditer(r"mul\(\d+,\d+\)", q)]
    dos = [i.start(0) for i in re.finditer(r"do\(\)", q)]
    donts = [i.start(0) for i in re.finditer(r"don't\(\)", q)]

    for i in dos:
        l0.append([i, 1])

    for i in donts:
        l0.append([i, 0])

    l0.sort()

    j0 = 0
    a = True

    for j in x:
        if y[j0] > l0[0][0]:
            for i in range(len(l0) - 1):
                if l0[i][0] < y[j0] and l0[i + 1][0] > y[j0] and l0[i][1] == 1:
                    a = True
                    break
                else:
                    a = False

        if a:
            a = j.replace("mul(", "").replace(")", "")
            res += int(a.split(",")[0]) * int(a.split(",")[1])

        j0 += 1

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
class _03_MullItOver_Test(unittest.TestCase):
    with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_03_MullItOver_Output.txt") as input:
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
