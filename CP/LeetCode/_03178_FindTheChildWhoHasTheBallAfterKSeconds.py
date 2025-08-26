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
with open(f"{cwd}/RftData/CP/LeetCode/IO/_03178_FindTheChildWhoHasTheBallAfterKSeconds_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion


# region Data Processing
def _03178_FindTheChildWhoHasTheBallAfterKSeconds_0() -> int:
    x = 0
    
    return x


# tic = timeit.default_timer()
print(f"_03178_FindTheChildWhoHasTheBallAfterKSeconds_0: {_03178_FindTheChildWhoHasTheBallAfterKSeconds_0()}")
# snapshot1 = tracemalloc.take_snapshot()
# toc = timeit.default_timer()
# elapsed_time = toc - tic
# print(f"Execution time: {elapsed_time:.8f}s\n")
# endregion


# region Unit Testing
class _03178_FindTheChildWhoHasTheBallAfterKSeconds_Test(unittest.TestCase):
    with open(
        f"{cwd}/RftData/CP/LeetCode/IO/_03178_FindTheChildWhoHasTheBallAfterKSeconds_Output.txt"
    ) as input:
        l = input.read().strip().splitlines()

    def test_03178_FindTheChildWhoHasTheBallAfterKSeconds_0(self):
        self.assertEqual(_03178_FindTheChildWhoHasTheBallAfterKSeconds_0(), int(self.l[0]))


unittest.main(argv=[""], verbosity=1, exit=False)

# region Memory Profiling
# top_stats = snapshot1.statistics("lineno")
# for i in top_stats:
#     print(i)
# endregion
