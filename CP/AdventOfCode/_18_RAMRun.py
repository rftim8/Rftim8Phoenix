from collections import deque
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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_18_RAMRun_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0

    a = list(l)
    n = 71
    g = [["." for c in range(n)] for r in range(n)]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for line in a[:1024]:
        x, y = [int(x) for x in line.split(",")]
        if 0 <= y < n and 0 <= x < n:
            g[y][x] = "#"

    q = deque([(0, 0, 0)])
    vis = set()
    while q:
        d, r, c = q.popleft()
        if (r, c) == (n - 1, n - 1):
            res = d
            break
        if (r, c) in vis:
            continue
        vis.add((r, c))
        for dr, dc in dirs:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < n and 0 <= cc < n and g[rr][cc] != "#":
                q.append((d + 1, rr, cc))

    return res


def part_two() -> str:
    res = ""

    a = list(l)
    n = 71
    g = [["." for c in range(n)] for r in range(n)]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i, line in enumerate(a):
        x, y = [int(x) for x in line.split(",")]
        if 0 <= y < n and 0 <= x < n:
            g[y][x] = "#"

        q = deque([(0, 0, 0)])
        vis = set()
        f = False
        while q:
            d, r, c = q.popleft()
            if (r, c) == (n - 1, n - 1):
                if i == 1023:
                    res = d
                f = True
                break
            if (r, c) in vis:
                continue
            vis.add((r, c))
            for dr, dc in dirs:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < n and 0 <= cc < n and g[rr][cc] != "#":
                    q.append((d + 1, rr, cc))

        if not f:
            # print(i)
            res = f"{x},{y}"
            return res

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
class _18_RAMRun_Test(unittest.TestCase):
    with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_18_RAMRun_Output.txt") as input:
        l = input.read().strip().splitlines()

    def test_part_one(self):
        self.assertEqual(part_one(), int(self.l[0]))

    def test_part_two(self):
        self.assertEqual(part_two(), self.l[1])


unittest.main(argv=[""], verbosity=1, exit=False)

# region Memory Profiling
# top_stats = snapshot1.statistics("lineno")
# for i in top_stats:
#     print(i)
# endregion
