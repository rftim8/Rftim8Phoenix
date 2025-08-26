import os


os.system("cls")
cwd = os.getcwd()


N = {
    (x, y): int(v)
    for y, l in enumerate(
        open(f"{cwd}/CP/AdventOfCode/_2021_Event/_11_DumboOctopus.txt")
        .read()
        .splitlines()
    )
    for x, v in enumerate(l)
}
Z = [-1, 0, 1]


def u():
    u = {}
    m = (
        lambda p: N[p]
        + 1
        + sum(map(lambda i: i in u, [(p[0] + a, p[1] + b) for a in Z for b in Z]))
    )
    l = -1
    while len(u) > l:
        l = len(u)
        u = set(p for p in N if m(p) > 9)
    return {k: 0 if k in u else m(k) for k in N}, len(u)


S = []
s = 0
while len(N) > s:
    N, s = u()
    S += [s]

print("Part 1: {:d}".format(sum(S[:100])))
print("Part 2: {:d}".format(len(S)))
