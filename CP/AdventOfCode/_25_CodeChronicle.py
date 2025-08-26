from io import StringIO
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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_25_CodeChronicle_Input.txt") as input:
    l = input.read().split("\n\n")
# endregion


# region Data Processing
def part_one() -> int:
    locks, keys = [], []
    height = 0

    data = list(l)

    for element in data:
        field = np.genfromtxt(StringIO(element), dtype=str, comments="_", delimiter=1)
        height = field.shape[0]
        value = np.sum(field == "#", axis=0)
        keys.append(value) if np.any(field[-1, :] == "#") else locks.append(value)

    res = sum([np.all(lock + key <= height) for key in keys for lock in locks])

    return res


# tic = timeit.default_timer()
print(f"Part One: {part_one()}")
# snapshot1 = tracemalloc.take_snapshot()
# toc = timeit.default_timer()
# elapsed_time = toc - tic
# print(f"Execution time: {elapsed_time:.8f}s\n")
# endregion


# region Unit Testing
class _25_CodeChronicle_Test(unittest.TestCase):
    with open(
        f"{cwd}/RftData/CP/AdventOfCode/IO/_25_CodeChronicle_Output.txt"
    ) as input:
        l = input.read().split("\n\n")

    def test_part_one(self):
        self.assertEqual(part_one(), int(self.l[0]))


unittest.main(argv=[""], verbosity=1, exit=False)

# region Memory Profiling
# top_stats = snapshot1.statistics("lineno")
# for i in top_stats:
#     print(i)
# endregion
