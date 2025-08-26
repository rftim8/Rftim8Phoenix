from itertools import product
import os
import unittest
import sys

os.system("cls")
cwd = os.getcwd()
sys.path.append(cwd)


# tracemalloc.start()

# region Data Gathering
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_07_BridgeRepair_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def part_one() -> int:
    res = 0

    for i in l:
        a = int(i.split(":")[0])
        b = [int(j) for j in i.split(":")[1][1:].split(" ")]
        q = product([0, 1], repeat=len(b))
        f = True
        for j in q:
            if f:
                c = 0
                for k in range(len(j)):
                    if j[k] == 1:
                        if k == 0:
                            c = 1
                        c *= b[k]
                    else:
                        c += b[k]
                    if c == a:
                        res += a
                        f = False
                        break
                # print(f"{a} {c}")

    return res


def part_two() -> int:
    res = 0

    for i in l:
        a = int(i.split(":")[0])
        b = [int(j) for j in i.split(":")[1][1:].split(" ")]
        q = product([0, 1, 2], repeat=len(b))
        f = True
        for j in q:
            # print(j)
            if f:
                c = 0
                for k in range(len(j)):
                    if j[k] == 1:
                        if k == 0:
                            c = 1
                        c *= b[k]
                    elif j[k] == 0:
                        c += b[k]
                    else:
                        c = int(str(c) + str(b[k]))
                if c == a:
                    res += a
                    f = False
                    break
                # print(f"{a} {c}")

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
class _07_BridgeRepair_Test(unittest.TestCase):
    with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_07_BridgeRepair_Output.txt") as input:
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
