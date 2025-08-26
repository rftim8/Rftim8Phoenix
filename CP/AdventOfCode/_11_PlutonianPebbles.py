import os
from typing import List
import numpy as np
import timeit
import tracemalloc
import unittest
from os import path
import sys

sys.setrecursionlimit(10**6)
os.system("cls")
cwd = os.getcwd()
sys.path.append(cwd)


# tracemalloc.start()

# region Data Gathering
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_11_PlutonianPebbles_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0

    a = [int(i) for i in l[0].split(" ")]

    for _ in range(25):
        i = 0
        while i < len(a):
            if a[i] == 0:
                a[i] = 1
            else:
                t = str(a[i])
                t0 = len(t)
                t1 = int(t0 / 2)
                if t0 % 2 == 0:
                    a.pop(i)
                    a.insert(i, int(t[t1:]))
                    a.insert(i, int(t[:t1]))
                    i += 1
                else:
                    a[i] *= 2024
            i += 1

    res += len(a)

    return res


def part_two() -> int:
    res = 0

    a = [int(i) for i in l[0].split(" ")]
    DP = {}

    def solve(x, t):
        if (x, t) in DP:
            return DP[(x, t)]
        if t == 0:
            ret = 1
        elif x == 0:
            ret = solve(1, t - 1)
        elif len(str(x)) % 2 == 0:
            dstr = str(x)
            left = dstr[: len(dstr) // 2]
            right = dstr[len(dstr) // 2 :]
            left, right = (int(left), int(right))
            ret = solve(left, t - 1) + solve(right, t - 1)
        else:
            ret = solve(x * 2024, t - 1)
        DP[(x, t)] = ret
        return ret

    res = sum(solve(x, 75) for x in a)

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
class _11_PlutonianPebbles_Test(unittest.TestCase):
    with open(
        f"{cwd}/RftData/CP/AdventOfCode/IO/_11_PlutonianPebbles_Output.txt"
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
