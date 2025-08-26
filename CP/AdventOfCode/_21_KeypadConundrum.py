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
with open(f"{cwd}/RftData/CP/AdventOfCode/IO/_21_KeypadConundrum_Input.txt") as input:
    l = input.read().strip().splitlines()
# endregion

FIRST_PAD = {
    c: (row, col)
    for row, line in enumerate("789\n456\n123\n 0A".splitlines())
    for col, c in enumerate(line)
    if c != " "
}

SECOND_PAD = {
    c: (row, col)
    for row, line in enumerate(" ^A\n<v>".splitlines())
    for col, c in enumerate(line)
    if c != " "
}


def generate_sequences_from_letter_to_letter(key_pad, start, end):
    to_check = [(start, "")]
    while to_check:
        current_position, path = to_check.pop()

        target = key_pad[end]
        if current_position == key_pad[end]:
            yield path
            continue

        column_move = target[1] - current_position[1]
        if column_move != 0:
            new_point = current_position[0], current_position[1] + (
                column_move // abs(column_move)
            )
            if new_point in key_pad.values():
                if column_move > 0:
                    to_check.append((new_point, path + ">"))
                elif column_move < 0:
                    to_check.append((new_point, path + "<"))

        row_move = target[0] - current_position[0]
        if row_move != 0:
            new_point = (
                current_position[0] + (row_move // abs(row_move)),
                current_position[1],
            )
            if new_point in key_pad.values():
                if row_move > 0:
                    to_check.append((new_point, path + "v"))
                elif row_move < 0:
                    to_check.append((new_point, path + "^"))


cache = {
    # key_pad, deep, code
}


def get_minimal_sequence_length(key_pad, code, robots):
    if (len(key_pad), code, robots) in cache:
        return cache[len(key_pad), code, robots]

    if robots == 0:
        cache[len(key_pad), code, robots] = len(code)
        return len(code)

    current_position = key_pad["A"]
    minimal_length = 0
    new_robots = robots - 1

    for letter in code:
        minimal_length += min(
            get_minimal_sequence_length(SECOND_PAD, sequence + "A", new_robots)
            for sequence in generate_sequences_from_letter_to_letter(
                key_pad, current_position, letter
            )
        )

        current_position = key_pad[letter]

    cache[len(key_pad), code, robots] = minimal_length
    return minimal_length


# region Data Processing
def part_one() -> int:
    res = 0

    grid = list(l)

    for code in grid:
        min_value = get_minimal_sequence_length(FIRST_PAD, code, 3)

        res += min_value * int("".join(c for c in code if c in "1234567890"))

    return res


def part_two() -> int:
    res = 0

    grid = list(l)

    for code in grid:
        min_value = get_minimal_sequence_length(FIRST_PAD, code, 26)

        res += min_value * int("".join(c for c in code if c in "1234567890"))

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
class _21_KeypadConundrum_Test(unittest.TestCase):
    with open(
        f"{cwd}/RftData/CP/AdventOfCode/IO/_21_KeypadConundrum_Output.txt"
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
