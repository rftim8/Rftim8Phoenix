from functools import cmp_to_key
import os


os.system("cls")
cwd = os.getcwd()

lines = open(f"{cwd}/CP/AdventOfCode/_2022_Event/_13_DistressSignal.txt").read()

pairs = [list(map(eval, x.splitlines())) for x in lines.split("\n\n")]


def compare(left, right):
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]
    for l, r in zip(left, right):
        if isinstance(l, list) or isinstance(r, list):
            res = compare(l, r)
        else:
            res = r - l
        if res != 0:
            return res
    return len(right) - len(left)


part1 = sum(i for i, (left, right) in enumerate(pairs, 1) if compare(left, right) > 0)

part2 = 1
sorted_list = sorted(
    [y for x in pairs for y in x] + [[[2]], [[6]]],
    key=cmp_to_key(compare),
    reverse=True,
)
for i, item in enumerate(sorted_list, 1):
    if item in ([[2]], [[6]]):
        part2 *= i

print(part1)
print(part2)
