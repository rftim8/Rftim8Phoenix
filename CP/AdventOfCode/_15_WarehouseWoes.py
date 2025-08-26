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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_15_WarehouseWoes_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    a = []
    instrs = ""
    f = True
    for i in l:
        if i == "":
            f = False
        else:
            if f:
                a.append(i)
            else:
                instrs += i

    nr = len(a)
    nc = len(a[0])
    a = [[a[r][c] for c in range(nc)] for r in range(nr)]

    for r in range(nr):
        for c in range(nc):
            if a[r][c] == "@":
                sr, sc = r, c
                a[r][c] = "."

    r, c = sr, sc
    for inst in instrs:
        dr, dc = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}[inst]
        rr, cc = r + dr, c + dc
        if a[rr][cc] == "#":
            continue
        elif a[rr][cc] == ".":
            r, c = rr, cc
        elif a[rr][cc] in ["[", "]", "O"]:
            dq = deque([(r, c)])
            vis = set()
            ok = True
            while dq:
                rr, cc = dq.popleft()
                if (rr, cc) in vis:
                    continue
                vis.add((rr, cc))
                rrr, ccc = rr + dr, cc + dc
                if a[rrr][ccc] == "#":
                    ok = False
                    break
                if a[rrr][ccc] == "O":
                    dq.append((rrr, ccc))
                if a[rrr][ccc] == "[":
                    dq.append((rrr, ccc))
                    assert a[rrr][ccc + 1] == "]"
                    dq.append((rrr, ccc + 1))
                if a[rrr][ccc] == "]":
                    dq.append((rrr, ccc))
                    assert a[rrr][ccc - 1] == "["
                    dq.append((rrr, ccc - 1))
            if not ok:
                continue
            while len(vis) > 0:
                for rr, cc in sorted(vis):
                    rrr, ccc = rr + dr, cc + dc
                    if (rrr, ccc) not in vis:
                        assert a[rrr][ccc] == "."
                        a[rrr][ccc] = a[rr][cc]
                        a[rr][cc] = "."
                        vis.remove((rr, cc))
            r = r + dr
            c = c + dc

    res = 0

    for r in range(nr):
        for c in range(nc):
            if a[r][c] in ["[", "O"]:
                res += 100 * r + c

    return res


def part_two() -> int:
    a = []
    instrs = ""
    f = True
    for i in l:
        if i == "":
            f = False
        else:
            if f:
                a.append(i)
            else:
                instrs += i

    nr = len(a)
    nc = len(a[0])
    a = [[a[r][c] for c in range(nc)] for r in range(nr)]
    a0 = []
    for r in range(nr):
        row = []
        for c in range(nc):
            if a[r][c] == "#":
                row.append("#")
                row.append("#")
            if a[r][c] == "O":
                row.append("[")
                row.append("]")
            if a[r][c] == ".":
                row.append(".")
                row.append(".")
            if a[r][c] == "@":
                row.append("@")
                row.append(".")
        a0.append(row)
    a = a0
    nc *= 2

    for r in range(nr):
        for c in range(nc):
            if a[r][c] == "@":
                sr, sc = r, c
                a[r][c] = "."

    r, c = sr, sc
    for inst in instrs:
        dr, dc = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}[inst]

        rr, cc = r + dr, c + dc
        if a[rr][cc] == "#":
            continue
        elif a[rr][cc] == ".":
            r, c = rr, cc
        elif a[rr][cc] in ["[", "]", "O"]:
            q = deque([(r, c)])
            vis = set()
            ok = True
            while q:
                rr, cc = q.popleft()
                if (rr, cc) in vis:
                    continue
                vis.add((rr, cc))
                rrr, ccc = rr + dr, cc + dc
                if a[rrr][ccc] == "#":
                    ok = False
                    break
                if a[rrr][ccc] == "O":
                    q.append((rrr, ccc))
                if a[rrr][ccc] == "[":
                    q.append((rrr, ccc))
                    assert a[rrr][ccc + 1] == "]"
                    q.append((rrr, ccc + 1))
                if a[rrr][ccc] == "]":
                    q.append((rrr, ccc))
                    assert a[rrr][ccc - 1] == "["
                    q.append((rrr, ccc - 1))
            if not ok:
                continue
            while len(vis) > 0:
                for rr, cc in sorted(vis):
                    rrr, ccc = rr + dr, cc + dc
                    if (rrr, ccc) not in vis:
                        assert a[rrr][ccc] == "."
                        a[rrr][ccc] = a[rr][cc]
                        a[rr][cc] = "."
                        vis.remove((rr, cc))
            r = r + dr
            c = c + dc

    res = 0

    for r in range(nr):
        for c in range(nc):
            if a[r][c] in ["[", "O"]:
                res += 100 * r + c

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
class _15_WarehouseWoes_Test(unittest.TestCase):
    with open(
        f"{cwd}/RftData/CP/AdventOfCode/IO/_15_WarehouseWoes_Output.txt"
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
