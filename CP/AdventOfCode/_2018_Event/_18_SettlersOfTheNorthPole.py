import os
import numpy as np
from collections import defaultdict

os.system("cls")
cwd = os.getcwd()

with open(f"{cwd}/CP/AdventOfCode/_2018_Event/_18_SettlersOfTheNorthPole.txt") as f:
    d = np.array([[y for y in x] for x in f.read().splitlines()], dtype=np.character)

scores = defaultdict(set, {})

for i in range(1000000000):
    nd = d.copy()
    for x in range(d.shape[0]):
        for y in range(d.shape[1]):
            if d[x, y] == b".":
                if (
                    np.count_nonzero(
                        d[max(0, x - 1) : x + 2, max(0, y - 1) : y + 2] == b"|"
                    )
                    >= 3
                ):
                    nd[x, y] = b"|"
            elif d[x, y] == b"|":
                if (
                    np.count_nonzero(
                        d[max(0, x - 1) : x + 2, max(0, y - 1) : y + 2] == b"#"
                    )
                    >= 3
                ):
                    nd[x, y] = b"#"
            elif d[x, y] == b"#":
                if (
                    np.count_nonzero(
                        d[max(0, x - 1) : x + 2, max(0, y - 1) : y + 2] == b"#"
                    )
                    < 2
                    or np.count_nonzero(
                        d[max(0, x - 1) : x + 2, max(0, y - 1) : y + 2] == b"|"
                    )
                    == 0
                ):
                    nd[x, y] = b"."
    d = nd
    score = np.count_nonzero(d == b"#") * np.count_nonzero(d == b"|")
    if i == 9:
        print("Part 1: ", score)
    if score in scores:
        if len(scores[score]) > 3:
            if (i + 1) % (i - sorted(scores[score])[-1]) == 1000000000 % (
                i - sorted(scores[score])[-1]
            ):
                print("Part 2: ", score)
                break
    scores[score].add(i)
