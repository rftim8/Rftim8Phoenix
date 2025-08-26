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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_10_HoofIt_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0

    a = list(l)
    R = len(a)
    C = len(a[0])

    for sr in range(R):
        for sc in range(C):
            if a[sr][sc] == "0":
                Q = deque([(0, sr, sc)])
                SEEN = set()
                while Q:
                    d, r, c = Q.popleft()
                    if (r, c) in SEEN:
                        continue
                    SEEN.add((r, c))
                    if a[r][c] == "9":
                        res += 1
                    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        rr = r + dr
                        cc = c + dc
                        if (
                            0 <= rr < R
                            and 0 <= cc < C
                            and int(a[rr][cc]) == int(a[r][c]) + 1
                        ):
                            Q.append((d + 1, rr, cc))

    return res


def part_two() -> int:
    res = 0

    a = list(l)
    R = len(a)
    C = len(a[0])

    DP = {}

    def ways(r, c):
        if a[r][c] == "0":
            return 1
        if (r, c) in DP:
            return DP[(r, c)]
        ans = 0
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C and int(a[rr][cc]) == int(a[r][c]) - 1:
                ans += ways(rr, cc)
        DP[(r, c)] = ans
        return ans

    for r in range(R):
        for c in range(C):
            if a[r][c] == "9":
                res += ways(r, c)

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
class _10_HoofIt_Test(unittest.TestCase):
    with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_10_HoofIt_Output.txt") as input:
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
