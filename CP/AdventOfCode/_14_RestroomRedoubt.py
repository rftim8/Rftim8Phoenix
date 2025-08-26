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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_14_RestroomRedoubt_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0

    d = 100

    cx = 101
    cy = 103

    map = []
    for i in range(cy):
        map.append("." * cx)

    r = []
    a = list(l)
    for i in a:
        p = i.split("=")[1].split(" ")[0]
        x = int(p.split(",")[0])
        y = int(p.split(",")[1])
        p = i.split("=")[2]
        vx = int(p.split(",")[0])
        vy = int(p.split(",")[1])

        for _ in range(d):
            y += vy
            if y < 0:
                y = cy - y * -1
            elif y > cy - 1:
                y = y - cy

            x += vx
            if x < 0:
                x = cx - x * -1
            elif x > cx - 1:
                x = x - cx

        r.append((y, x))

    for i in r:
        if map[i[0]][i[1]] == ".":
            map[i[0]] = map[i[0]][: i[1]] + "1" + map[i[0]][i[1] + 1 :]
        else:
            map[i[0]] = (
                map[i[0]][: i[1]]
                + str(int(map[i[0]][i[1]]) + 1)
                + map[i[0]][i[1] + 1 :]
            )

    hx = (cx - 1) / 2
    hy = (cy - 1) / 2
    (q0, q1, q2, q3) = (0, 0, 0, 0)
    for i in range(cy):
        for j in range(cx):
            if map[i][j] != ".":
                t = int(map[i][j])
                if i < hy and j < hx:
                    q0 += t
                elif i < hy and j > hx:
                    q1 += t
                elif i > hy and j < hx:
                    q2 += t
                elif i > hy and j > hx:
                    q3 += t

    # for i in map:
    #     print(i)

    res = q0 * q1 * q2 * q3

    return res


def part_two() -> int:
    res = 0
    a = list(l)

    cx = 103
    cy = 101

    map = []
    for i in range(cy):
        map.append("." * cx)

    # quads = [0, 0, 0, 0]
    # hx = (cx - 1) / 2
    # hy = (cy - 1) / 2

    for steps in range(1, 100000):
        r = set()
        for i in a:
            p = i.split("=")[1].split(" ")[0]
            px = int(p.split(",")[0])
            py = int(p.split(",")[1])
            p = i.split("=")[2]
            vx = int(p.split(",")[0])
            vy = int(p.split(",")[1])

            nx = (px + steps * vx) % 101
            ny = (py + steps * vy) % 103

            # if nx < hx and ny < hy:
            #     quads[0] += 1
            # elif nx > hx and ny < hy:
            #     quads[1] += 1
            # elif nx < hx and ny > hy:
            #     quads[2] += 1
            # elif nx > hx and ny > hy:
            #     quads[3] += 1

            # res = quads[0] * quads[1] * quads[2] * quads[3]

            r.add((nx, ny))

        if len(r) == len(a):
            res = steps
            break

    # print Easter Egg: Christmas Tree
    # print(
    #     "\n".join(
    #         "".join(" " if (x, y) not in r else "#" for x in range(103))
    #         for y in range(101)
    #     )
    # )

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
class _14_RestroomRedoubt_Test(unittest.TestCase):
    with open(
        f"{cwd}/RftData/CP/AdventOfCode/IO/_14_RestroomRedoubt_Output.txt"
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
