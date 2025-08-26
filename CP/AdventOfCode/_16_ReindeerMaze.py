import heapq
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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_16_ReindeerMaze_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    g = list(l)
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    nr = len(g)
    nc = len(g[0])
    g = [[g[r][c] for c in range(nc)] for r in range(nr)]

    for r in range(nr):
        for c in range(nc):
            if g[r][c] == "S":
                sr, sc = r, c
            if g[r][c] == "E":
                er, ec = r, c

    q = []
    vis = set()
    heapq.heappush(q, (0, sr, sc, 1))
    dist = {}
    res = None
    while q:
        d, r, c, dir = heapq.heappop(q)
        if (r, c, dir) not in dist:
            dist[(r, c, dir)] = d
        if r == er and c == ec and res is None:
            res = d
        if (r, c, dir) in vis:
            continue
        vis.add((r, c, dir))
        dr, dc = dirs[dir]
        rr, cc = r + dr, c + dc
        if 0 <= cc < nc and 0 <= rr < nr and g[rr][cc] != "#":
            heapq.heappush(q, (d + 1, rr, cc, dir))
        heapq.heappush(q, (d + 1000, r, c, (dir + 1) % 4))
        heapq.heappush(q, (d + 1000, r, c, (dir + 3) % 4))

    return res


def part_two() -> int:
    res = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    g = list(l)
    nr = len(g)
    nc = len(g[0])
    g = [[g[r][c] for c in range(nc)] for r in range(nr)]

    for r in range(nr):
        for c in range(nc):
            if g[r][c] == "S":
                sr, sc = r, c
            if g[r][c] == "E":
                er, ec = r, c
    q = []
    vis = set()
    heapq.heappush(q, (0, sr, sc, 1))
    dist = {}
    best = None
    while q:
        d, r, c, dir = heapq.heappop(q)
        if (r, c, dir) not in dist:
            dist[(r, c, dir)] = d
        if r == er and c == ec and best is None:
            best = d
        if (r, c, dir) in vis:
            continue
        vis.add((r, c, dir))
        dr, dc = dirs[dir]
        rr, cc = r + dr, c + dc
        if 0 <= cc < nc and 0 <= rr < nr and g[rr][cc] != "#":
            heapq.heappush(q, (d + 1, rr, cc, dir))
        heapq.heappush(q, (d + 1000, r, c, (dir + 1) % 4))
        heapq.heappush(q, (d + 1000, r, c, (dir + 3) % 4))

    q = []
    vis = set()
    for dir in range(4):
        heapq.heappush(q, (0, er, ec, dir))
    dist2 = {}
    while q:
        d, r, c, dir = heapq.heappop(q)
        if (r, c, dir) not in dist2:
            dist2[(r, c, dir)] = d
        if (r, c, dir) in vis:
            continue
        vis.add((r, c, dir))
        dr, dc = dirs[(dir + 2) % 4]
        rr, cc = r + dr, c + dc
        if 0 <= cc < nc and 0 <= rr < nr and g[rr][cc] != "#":
            heapq.heappush(q, (d + 1, rr, cc, dir))
        heapq.heappush(q, (d + 1000, r, c, (dir + 1) % 4))
        heapq.heappush(q, (d + 1000, r, c, (dir + 3) % 4))

    s = set()
    for r in range(nr):
        for c in range(nc):
            for dir in range(4):
                if (
                    (r, c, dir) in dist
                    and (r, c, dir) in dist2
                    and dist[(r, c, dir)] + dist2[(r, c, dir)] == best
                ):
                    s.add((r, c))
    res = len(s)

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
class _16_ReindeerMaze_Test(unittest.TestCase):
    with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_16_ReindeerMaze_Output.txt") as input:
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
