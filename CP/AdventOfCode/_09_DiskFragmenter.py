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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_09_DiskFragmenter_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0

    a = l[0]
    b = list()
    c = 0
    f = 1
    for i in a:
        if f > 0:
            for j in range(int(i)):
                b.append(c)
            c += 1
        else:
            for j in range(int(i)):
                b.append(".")

        f *= -1

    for i in range(len(b) - 1, 0, -1):
        for j in range(len(b)):
            if b[j] == "." and j < i:
                t = b[i]
                b[i] = b[j]
                b[j] = t
                break

    c = 0
    for i in b:
        if i != ".":
            res += c * int(i)
        c += 1

    return res


def part_two() -> int:
    res = 0
    a = l[0]

    A = deque([])
    SPACE = deque([])
    pos = 0
    file_id = 0
    FINAL = []
    for i, c in enumerate(a):
        if i % 2 == 0:
            A.append((pos, int(c), file_id))
            for _ in range(int(c)):
                FINAL.append(file_id)
                pos += 1
            file_id += 1
        else:
            SPACE.append((pos, int(c)))
            for _ in range(int(c)):
                FINAL.append(".")
                pos += 1

    for pos, sz, file_id in reversed(A):
        for space_i, (space_pos, space_sz) in enumerate(SPACE):
            if space_pos < pos and sz <= space_sz:
                for i in range(sz):
                    assert FINAL[pos + i] == file_id
                    FINAL[pos + i] = "."
                    FINAL[space_pos + i] = file_id
                SPACE[space_i] = (space_pos + sz, space_sz - sz)
                break

    for i, c in enumerate(FINAL):
        if c is not ".":
            res += i * c

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
class _09_DiskFragmenter_Test(unittest.TestCase):
    with open(
        f"{cwd}/RftData/CP/AdventOfCode/IO/_09_DiskFragmenter_Output.txt"
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
