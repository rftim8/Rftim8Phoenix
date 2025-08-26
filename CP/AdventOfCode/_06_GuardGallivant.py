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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_06_GuardGallivant_Input.txt") as input:
    l1 = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    l = list(l1)
    res = 0

    x = 0
    y = 0

    a = len(l)
    b = len(l[0])

    for i in range(a):
        l[i] = f",{l[i]},"

    s = ""
    for i in range(b + 2):
        s += ","

    l.insert(0, s)
    l.append(s)

    for i in range(a + 2):
        for j in range(b + 2):
            if l[i][j] == "^":
                x = i
                y = j

    l0 = list(l)
    loc = set()
    while l[x][y] != ",":
        if l[x][y] == "^":
            t = l0[x][:y] + "X" + l0[x][y + 1 :]
            l0[x] = t
            loc.add((x, y))
            if l[x - 1][y] == "#":
                t = l[x][:y] + ">" + l[x][y + 1 :]
                l[x] = t
            elif l[x - 1][y] == ".":
                t = l[x][:y] + "." + l[x][y + 1 :]
                l[x] = t
                t = l[x - 1][:y] + "^" + l[x - 1][y + 1 :]
                l[x - 1] = t
            if l[x - 1][y] != "#":
                x -= 1
        elif l[x][y] == ">":
            t = l0[x][:y] + "X" + l0[x][y + 1 :]
            l0[x] = t
            loc.add((x, y))
            if l[x][y + 1] == "#":
                t = l[x][:y] + "v" + l[x][y + 1 :]
                l[x] = t
            elif l[x][y + 1] == ".":
                t = l[x][:y] + "." + l[x][y + 1 :]
                l[x] = t
                t = l[x][: y + 1] + ">" + l[x][y + 2 :]
                l[x] = t
            if l[x][y + 1] != "#":
                y += 1
        elif l[x][y] == "v":
            t = l0[x][:y] + "X" + l0[x][y + 1 :]
            l0[x] = t
            loc.add((x, y))
            if l[x + 1][y] == "#":
                t = l[x][:y] + "<" + l[x][y + 1 :]
                l[x] = t
            elif l[x + 1][y] == ".":
                t = l[x][:y] + "." + l[x][y + 1 :]
                l[x] = t
                t = l[x + 1][:y] + "v" + l[x + 1][y + 1 :]
                l[x + 1] = t
            if l[x + 1][y] != "#":
                x += 1
        elif l[x][y] == "<":
            t = l0[x][:y] + "X" + l0[x][y + 1 :]
            l0[x] = t
            loc.add((x, y))
            if l[x][y - 1] == "#":
                t = l[x][:y] + "^" + l[x][y + 1 :]
                l[x] = t
            elif l[x][y - 1] == ".":
                t = l[x][:y] + "." + l[x][y + 1 :]
                l[x] = t
                t = l[x][: y - 1] + "<" + l[x][y:]
                l[x] = t
            if l[x][y - 1] != "#":
                y -= 1

    res = len(loc)

    return res


def part_two() -> int:
    l = list(l1)
    p2 = 0
    p1 = 0

    x = len(l)
    y = len(l[0])
    for i in range(x):
        for j in range(y):
            if l[i][j] == "^":
                sr, sc = i, j

    for o_r in range(x):
        for o_c in range(y):
            r, c = sr, sc
            d = 0
            obs = set()
            steps = set()
            while True:
                if (r, c, d) in obs:
                    p2 += 1
                    break
                obs.add((r, c, d))
                steps.add((r, c))
                dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
                rr = r + dr
                cc = c + dc
                if not (0 <= rr < x and 0 <= cc < y):
                    if l[o_r][o_c] == "#":
                        p1 = len(steps)
                    break
                if l[rr][cc] == "#" or rr == o_r and cc == o_c:
                    d = (d + 1) % 4
                else:
                    r = rr
                    c = cc

    return p2


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
class _06_GuardGallivant_Test(unittest.TestCase):
    with open(
        f"{cwd}/RftData/CP/AdventOfCode/IO/_06_GuardGallivant_Output.txt"
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
