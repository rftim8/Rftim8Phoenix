import os

os.system("cls")
cwd = os.getcwd()

input = [
    i.splitlines()
    for i in (
        open(f"{cwd}/CP/AdventOfCode/_2023_Event/_05_IfYouGiveASeedAFertilizer.txt")
        .read()
        .split("\n\n")
    )
]

seeds = [int(i) for i in input[0][0].split()[1:]]
maps = [[[int(i) for i in l.split()] for l in b[1:]] for b in input[1:]]

# PartOne
# ranges = [ ( i, 1 ) for i in seeds ]

# PartTwo
ranges = list(zip(seeds[::2], seeds[1::2]))

for map in maps:
    r = []
    for seed, soil, rlen in map:
        i = 0
        while i < len(ranges):
            item1, item2 = ranges[i]
            if soil <= item1 < soil + rlen <= item1 + item2:
                r.append((item1 - soil + seed, soil + rlen - item1))
                ranges[i] = (soil + rlen, item1 + item2 - soil - rlen)
            elif item1 <= soil < item1 + item2 <= soil + rlen:
                r.append((seed, item1 + item2 - soil))
                ranges[i] = (item1, soil - item1)
            elif item1 <= soil < soil + rlen <= item1 + item2:
                r.append((seed, rlen))
                ranges[i] = (item1, soil - item1)
                ranges.append((soil + rlen, item1 + item2 - soil - rlen))
            if soil <= item1 < item1 + item2 <= soil + rlen:
                r.append((item1 - soil + seed, item2))
                ranges[i] = ranges[-1]
                del ranges[-1]
            else:
                i += 1
    ranges += r

print(min(item1 for item1, item2 in ranges))
