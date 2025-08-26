from copy import deepcopy
import os
import re
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
    f"{cwd}/RftData/CP/AdventOfCode/IO/_17_ChronospatialComputer_Input.txt"
) as input:
    l = input.read().strip().splitlines()
# endregion


def parse_data(my_file) -> tuple:
    with open(my_file) as f:
        registers, program = f.read().split("\n\n")
        registers = {
            (x := re.match("Register (\w): (\d+)", reg).groups())[0]: int(x[1])
            for reg in registers.split("\n")
        }
        registers |= {str(num): num for num in range(4)}
        program = [int(num) for num in re.findall("\d", program)]
        return registers, program


def run_prog(regs: dict, program: list) -> list:
    combos = "0123ABC"
    idx = 0
    out = []
    while idx < len(program):
        opcode = program[idx]
        operand = program[idx + 1]
        idx += 2
        match opcode:
            case 0 | 6 | 7:
                regs["A.....BC"[opcode]] = regs["A"] // 2 ** regs[combos[operand]]
            case 1 | 4:
                regs["B"] = regs["B"] ^ (operand if opcode == 1 else regs["C"])
            case 2:
                regs["B"] = regs[combos[operand]] % 8
            case 3:
                if regs["A"] != 0:
                    idx = operand
            case 5:
                out.append(regs[combos[operand]] % 8)
    return out


# region Data Processing
def part_one() -> str:
    g = list(l)
    f = True
    regs = dict()
    program = []
    for i in g:
        if i == "":
            f = False
        else:
            if f:
                regs[i.split(":")[0].split(" ")[1]] = int(i.split(": ")[1])
            else:
                program = [int(j) for j in i.split(" ")[1].split(",")]

    for i in range(4):
        regs[str(i)] = i

    # data = parse_data(
    #     f"{cwd}/RftData/CP/AdventOfCode/IO/_17_ChronospatialComputer_Input.txt"
    # )

    return ",".join(str(num) for num in run_prog(*deepcopy((regs, program))))


def part_two() -> int:
    g = list(l)
    f = True
    regs = dict()
    program = []
    for i in g:
        if i == "":
            f = False
        else:
            if f:
                regs[i.split(":")[0].split(" ")[1]] = int(i.split(": ")[1])
            else:
                program = [int(j) for j in i.split(" ")[1].split(",")]

    for i in range(4):
        regs[str(i)] = i

    final_As = [0]

    for level in range(-1, -17, -1):
        step = 8 ** (len(program) + level)
        new_As = []
        for final_A in final_As:
            for idx in range(8):
                new_A = final_A + step * idx
                regs["A"] = new_A
                if run_prog(regs, program)[level:] == program[level:]:
                    new_As.append(new_A)
        final_As = new_As

    return final_As[0]


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
class _17_ChronospatialComputer_Test(unittest.TestCase):
    with open(
        f"{cwd}/RftData/CP/AdventOfCode/IO/_17_ChronospatialComputer_Output.txt"
    ) as input:
        l = input.read().strip().splitlines()

    def test_part_one(self):
        self.assertEqual(part_one(), self.l[0])

    def test_part_two(self):
        self.assertEqual(part_two(), int(self.l[1]))


unittest.main(argv=[""], verbosity=1, exit=False)

# region Memory Profiling
# top_stats = snapshot1.statistics("lineno")
# for i in top_stats:
#     print(i)
# endregion
