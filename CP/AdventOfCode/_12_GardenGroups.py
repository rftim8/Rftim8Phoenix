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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_12_GardenGroups_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0

    a = list(l)
    b = len(a)
    c = len(a[0])

    for i in range(b):
        for j in range(c):
            if a[i][j] != ".":
                a0 = list(l)
                color = "."
                (sr, sc) = (i, j)
                old = a[sr][sc]
                st = deque()
                st.append((sr, sc))

                q = 0
                while len(st) > 0:
                    (y, x) = st.pop()

                    if y < 0 or x < 0 or y >= b or x >= c:
                        continue
                    if a[y][x] != old or a[y][x] == color:
                        continue

                    a[y] = a[y][:x] + str(color) + a[y][x + 1 :]
                    a0[y] = a0[y][:x] + str(color) + a0[y][x + 1 :]
                    q += 1

                    st.append((y - 1, x))
                    st.append((y + 1, x))
                    st.append((y, x - 1))
                    st.append((y, x + 1))

                q0 = 0
                for k in range(b):
                    for m in range(c):
                        if a0[k][m] == ".":
                            if m == 0:
                                q0 += 1
                            elif a0[k][m - 1] != ".":
                                q0 += 1

                            if m == c - 1:
                                q0 += 1
                            elif a0[k][m + 1] != ".":
                                q0 += 1

                            if k == 0:
                                q0 += 1
                            elif a0[k - 1][m] != ".":
                                q0 += 1

                            if k == b - 1:
                                q0 += 1
                            elif a0[k + 1][m] != ".":
                                q0 += 1
                    #     print(a0[k][m], end=" ")
                    # print()
                # print((q, q0))
                res += q * q0

    return res


def part_two() -> int:
    res = 0

    a = list(l)
    R = len(a)
    C = len(a[0])
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    SEEN = set()
    for r in range(R):
        for c in range(C):
            if (r, c) in SEEN:
                continue
            Q = deque([(r, c)])
            area = 0
            PERIM = dict()
            while Q:
                r2, c2 = Q.popleft()
                if (r2, c2) in SEEN:
                    continue
                SEEN.add((r2, c2))
                area += 1
                for dr, dc in DIRS:
                    rr = r2 + dr
                    cc = c2 + dc
                    if 0 <= rr < R and 0 <= cc < C and a[rr][cc] == a[r2][c2]:
                        Q.append((rr, cc))
                    else:
                        if (dr, dc) not in PERIM:
                            PERIM[(dr, dc)] = set()
                        PERIM[(dr, dc)].add((r2, c2))
            sides = 0
            for k, vs in PERIM.items():
                SEEN_PERIM = set()
                for pr, pc in vs:
                    if (pr, pc) not in SEEN_PERIM:
                        sides += 1
                        Q = deque([(pr, pc)])
                        while Q:
                            r2, c2 = Q.popleft()
                            if (r2, c2) in SEEN_PERIM:
                                continue
                            SEEN_PERIM.add((r2, c2))
                            for dr, dc in DIRS:
                                rr, cc = r2 + dr, c2 + dc
                                if (rr, cc) in vs:
                                    Q.append((rr, cc))
            res += area * sides

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
class _12_GardenGroups_Test(unittest.TestCase):
    with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_12_GardenGroups_Output.txt") as input:
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
