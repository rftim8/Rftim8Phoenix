from collections import defaultdict
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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_22_MonkeyMarket_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0
    grid = [int(i) for i in l]

    for n in grid:
        for _ in range(2000):
            n = (n ^ (n << 6)) % 16777216
            n = (n ^ (n >> 5)) % 16777216
            n = (n ^ (n << 11)) % 16777216
        res += n

    return res


def part_two() -> int:
    res = 0
    grid = [int(i) for i in l]

    total = defaultdict(int)
    for n in grid:
        seqs = dict()
        seq = (0, 0, 0, 0)
        for i in range(2000):
            prev = n % 10
            n = (n ^ (n << 6)) % 16777216
            n = (n ^ (n >> 5)) % 16777216
            n = (n ^ (n << 11)) % 16777216
            seq = (*seq[1:], n % 10 - prev)
            if i >= 3 and seq not in seqs:
                seqs[seq] = n % 10
        for s in seqs:
            total[s] += seqs[s]
    winner = sorted([(v, k) for k, v in total.items()])[-1]
    # print(f"Max profit: {winner[0]} with sequence {winner[1]}")
    res = winner[0]

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
class _22_MonkeyMarket_Test(unittest.TestCase):
    with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_22_MonkeyMarket_Output.txt") as input:
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
