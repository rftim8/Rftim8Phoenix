from collections import defaultdict
import os
from typing import List
import numpy as np
import timeit
import tracemalloc
import unittest
from os import path
import sys
import networkx as nx

os.system("cls")
cwd = os.getcwd()
sys.path.append(cwd)

# Bron–Kerbosch algorithm

# tracemalloc.start()

# region Data Gathering
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_23_LANParty_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0
    grid = list(l)
    g = defaultdict(set)
    for a, b in [line.split("-") for line in grid]:
        g[a].add(b)
        g[b].add(a)

    res = len(
        set(
            ",".join(sorted([c, a, b]))
            for c in g
            for a in g[c]
            for b in g[c]
            if c.startswith("t") and b in g[a]
        )
    )
    return res


def part_one_0() -> int:
    grid = list(l)
    G = nx.Graph()
    for line in grid:
        x, y = line.strip().split("-")
        G.add_edge(x, y)

    return len(
        [
            clique
            for clique in nx.enumerate_all_cliques(G)
            if len(clique) == 3 and any(n.startswith("t") for n in clique)
        ]
    )


def part_two() -> str:
    res = ""
    grid = list(l)
    g = defaultdict(set)
    for a, b in [line.split("-") for line in grid]:
        g[a].add(b)
        g[b].add(a)

    def find_clique(target_size=13):
        for c1 in g:
            for c2 in g[c1]:
                m = set.intersection(*({a} | g[a] for a in g[c1] if a != c2))
                if len(m) == target_size:
                    return sorted(m)

    res = ",".join(find_clique())
    return res


def part_two_0() -> str:
    grid = list(l)
    G = nx.Graph()
    for line in grid:
        x, y = line.strip().split("-")
        G.add_edge(x, y)

    max_interconnected = [clique for clique in nx.enumerate_all_cliques(G)][-1]
    return ",".join(sorted(max_interconnected))


# tic = timeit.default_timer()
print(f"Part One: {part_one()}")
print(f"Part One 0: {part_one_0()}")
# snapshot1 = tracemalloc.take_snapshot()
# toc = timeit.default_timer()
# elapsed_time = toc - tic
# print(f"Execution time: {elapsed_time:.8f}s\n")

# tic = timeit.default_timer()
print(f"Part Two: {part_two()}")
print(f"Part Two 0: {part_two_0()}")
# snapshot1 = tracemalloc.take_snapshot()
# toc = timeit.default_timer()
# elapsed_time = toc - tic
# print(f"Execution time: {elapsed_time:.8f}s")
# endregion


# region Unit Testing
class _23_LANParty_Test(unittest.TestCase):
    with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_23_LANParty_Output.txt") as input:
        l = input.read().strip().splitlines()

    def test_part_one(self):
        self.assertEqual(part_one(), int(self.l[0]))

    def test_part_one_0(self):
        self.assertEqual(part_one_0(), int(self.l[0]))

    def test_part_two(self):
        self.assertEqual(part_two(), self.l[1])

    def test_part_two_0(self):
        self.assertEqual(part_two_0(), self.l[1])


unittest.main(argv=[""], verbosity=1, exit=False)

# region Memory Profiling
# top_stats = snapshot1.statistics("lineno")
# for i in top_stats:
#     print(i)
# endregion

# Look for the clique of size 13
