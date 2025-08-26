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
with open(
    f"{cwd}/RftData/CP/AdventOfCode/IO/_08_ResonantCollinearity_Input.txt"
) as input:
    l1 = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0
    l = list(l1)

    d = {}
    rc = len(l)
    cc = len(l[0])

    for r in range(rc):
        for c in range(cc):
            if l[r][c] != ".":
                if l[r][c] not in d:
                    d[l[r][c]] = []
                d[l[r][c]].append((r, c))

    for i in d.items():
        for j in range(len(i[1])):
            for k in range(j + 1, len(i[1])):
                (fx0, fy0, fx1, fy1) = (0, 0, 0, 0)
                (cx0, cy0, cx1, cy1) = (i[1][j][0], i[1][j][1], i[1][k][0], i[1][k][1])
                x = abs(cx0 - cx1)
                y = abs(cy0 - cy1)
                if cy0 < cy1:
                    fy0 = cy0 - y
                    fy1 = cy1 + y
                elif cy0 > cy1:
                    fy0 = cy0 + y
                    fy1 = cy1 - y

                fx0 = cx0 - x
                fx1 = cx1 + x

                if 0 <= fx0 < rc and 0 <= fy0 < cc:
                    if l[fx0][fy0] != "#":
                        l[fx0] = l[fx0][:fy0] + "#" + l[fx0][fy0 + 1 :]
                        res += 1
                if 0 <= fx1 < rc and 0 <= fy1 < cc:
                    if l[fx1][fy1] != "#":
                        l[fx1] = l[fx1][:fy1] + "#" + l[fx1][fy1 + 1 :]
                        res += 1

    # for r in range(rc):
    #     for c in range(cc):
    #         print(l[r][c], end="")
    #     print()

    return res


def part_two() -> int:
    l = list(l1)

    d = {}
    rc = len(l)
    cc = len(l[0])

    for r in range(rc):
        for c in range(cc):
            if l[r][c] != ".":
                if l[r][c] not in d:
                    d[l[r][c]] = []
                d[l[r][c]].append((r, c))

    a = set()
    for i in d.items():
        for j in range(len(i[1])):
            for k in range(j + 1, len(i[1])):
                (cx0, cy0, cx1, cy1) = (i[1][j][0], i[1][j][1], i[1][k][0], i[1][k][1])
                x = abs(cx0 - cx1)
                y = abs(cy0 - cy1)
                # print((cx0, cy0, cx1, cy1))

                if cx0 < cx1 and cy0 < cy1:
                    (x0, y0) = (cx0, cy0)
                    while 0 <= x0 < rc and 0 <= y0 < cc:
                        l[x0] = l[x0][:y0] + "#" + l[x0][y0 + 1 :]
                        l[cx1] = l[cx1][:cy1] + "#" + l[cx1][cy1 + 1 :]
                        a.add((x0, y0))
                        x0 -= x
                        y0 -= y

                    (x0, y0) = (cx1, cy1)
                    while 0 <= x0 < rc and 0 <= y0 < cc:
                        l[x0] = l[x0][:y0] + "#" + l[x0][y0 + 1 :]
                        l[cx0] = l[cx0][:cy0] + "#" + l[cx0][cy0 + 1 :]
                        a.add((x0, y0))
                        x0 += x
                        y0 += y

                if cx0 < cx1 and cy0 > cy1:
                    (x0, y0) = (cx0, cy0)
                    while 0 <= x0 < rc and 0 <= y0 < cc:
                        l[x0] = l[x0][:y0] + "#" + l[x0][y0 + 1 :]
                        l[cx1] = l[cx1][:cy1] + "#" + l[cx1][cy1 + 1 :]
                        a.add((x0, y0))
                        x0 -= x
                        y0 += y

                    (x0, y0) = (cx1, cy1)
                    while 0 <= x0 < rc and 0 <= y0 < cc:
                        l[x0] = l[x0][:y0] + "#" + l[x0][y0 + 1 :]
                        l[cx0] = l[cx0][:cy0] + "#" + l[cx0][cy0 + 1 :]
                        a.add((x0, y0))
                        x0 += x
                        y0 -= y

    # for r in range(rc):
    #     for c in range(cc):
    #         print(l[r][c], end="")
    #     print()

    return len(a)


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
class _08_ResonantCollinearity_Test(unittest.TestCase):
    with open(
        f"{cwd}/RftData/CP/AdventOfCode/IO/_08_ResonantCollinearity_Output.txt"
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
