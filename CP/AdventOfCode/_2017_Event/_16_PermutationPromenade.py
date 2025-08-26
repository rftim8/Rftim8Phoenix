import re, os

os.system("cls")
cwd = os.getcwd()

line = list("abcdefghijklmnop")
l = (
    open(f"{cwd}/CP/AdventOfCode/_2017_Event/_16_PermutationPromenade.txt")
    .read()
    .strip()
)

loop = 1
done = False
mod = 1
while not done:
    for mv in l.split(","):
        if "x" in mv:
            a, b = map(lambda x: int(x), mv[1:].split("/"))
            line[a], line[b] = line[b], line[a]
        elif "p" in mv:
            a, b = map(lambda x: line.index(x), mv[1:].split("/"))
            line[a], line[b] = line[b], line[a]
        else:
            m = re.match("s(\d+)", mv)
            n = int(m.group(1))
            line = line[-n:] + line[: (16 - n)]
    out = "".join(line)
    if loop == 1:
        print(f"Part 1: {out}")
        seen = out
    elif out == seen and mod == 1:
        interval = loop - 1
        mod = (1000000000 % interval) + interval
    if mod > 1 and loop % mod == 0:
        print(f"Part 2: {out}")
        done = True
    loop += 1
