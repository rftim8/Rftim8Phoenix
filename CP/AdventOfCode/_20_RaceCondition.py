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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_20_RaceCondition_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    arr = np.array([list(i) for i in l])
    distanceMap = np.zeros_like(arr, int)
    ds = ((1, 0), (-1, 0), (0, 1), (0, -1))
    i, j = [val[0] for val in np.where(arr == "S")]
    arr = np.logical_or(arr == "E", arr == ".")
    distanceMap[i, j] = 1
    currVal = 1

    while True:
        for di, dj in ds:
            if arr[i + di, j + dj] and not distanceMap[i + di, j + dj]:
                currVal += 1
                distanceMap[i + di, j + dj] = currVal
                i, j = i + di, j + dj
                break
        else:
            break

    iGrid, jGrid = np.ogrid[: arr.shape[0], : arr.shape[1]]
    i, j = np.where(distanceMap)
    manhattanDistances = np.abs(i - iGrid[:, :, np.newaxis]) + np.abs(
        j - jGrid[:, :, np.newaxis]
    )
    mask1 = manhattanDistances <= 2
    diff = distanceMap[:, :, np.newaxis] - distanceMap[i, j]
    results = diff - manhattanDistances

    return np.sum(results[mask1] >= 100)


def part_two() -> int:
    arr = np.array([list(i) for i in l])
    distanceMap = np.zeros_like(arr, int)
    ds = ((1, 0), (-1, 0), (0, 1), (0, -1))
    i, j = [val[0] for val in np.where(arr == "S")]
    arr = np.logical_or(arr == "E", arr == ".")
    distanceMap[i, j] = 1
    currVal = 1

    while True:
        for di, dj in ds:
            if arr[i + di, j + dj] and not distanceMap[i + di, j + dj]:
                currVal += 1
                distanceMap[i + di, j + dj] = currVal
                i, j = i + di, j + dj
                break
        else:
            break

    iGrid, jGrid = np.ogrid[: arr.shape[0], : arr.shape[1]]
    i, j = np.where(distanceMap)
    manhattanDistances = np.abs(i - iGrid[:, :, np.newaxis]) + np.abs(
        j - jGrid[:, :, np.newaxis]
    )
    mask2 = manhattanDistances <= 20
    diff = distanceMap[:, :, np.newaxis] - distanceMap[i, j]
    results = diff - manhattanDistances

    return np.sum(results[mask2] >= 100)


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
class _20_RaceCondition_Test(unittest.TestCase):
    with open(
        f"{cwd}/RftData/CP/AdventOfCode/IO/_20_RaceCondition_Output.txt"
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
