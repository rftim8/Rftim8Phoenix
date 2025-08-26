from itertools import permutations
import os

os.system("cls")
cwd = os.getcwd()


P = list(
    map(
        int,
        open(f"{cwd}/CP/AdventOfCode/_2019_Event/_07_AmplificationCircuit.txt")
        .read()
        .strip()
        .split(","),
    )
)


def run(phase):
    p = P[:]
    ip = 0
    while True:
        cmd = p[ip]
        op = cmd % 100
        if op == 1:
            a1 = p[ip + 1] if cmd // 100 % 10 == 1 else p[p[ip + 1]]
            a2 = p[ip + 2] if cmd // 1000 % 10 == 1 else p[p[ip + 2]]
            p[p[ip + 3]] = a1 + a2
            ip += 4
        elif op == 2:
            a1 = p[ip + 1] if cmd // 100 % 10 == 1 else p[p[ip + 1]]
            a2 = p[ip + 2] if cmd // 1000 % 10 == 1 else p[p[ip + 2]]
            p[p[ip + 3]] = a1 * a2
            ip += 4
        elif op == 3:
            p[p[ip + 1]] = yield
            ip += 2
        elif op == 4:
            yield p[p[ip + 1]]
            ip += 2
        elif op == 5:
            a = p[ip + 1] if cmd // 100 % 10 == 1 else p[p[ip + 1]]
            if a != 0:
                ip = p[ip + 2] if cmd // 1000 % 10 == 1 else p[p[ip + 2]]
            else:
                ip += 3
        elif op == 6:
            a = p[ip + 1] if cmd // 100 % 10 == 1 else p[p[ip + 1]]
            if a == 0:
                ip = p[ip + 2] if cmd // 1000 % 10 == 1 else p[p[ip + 2]]
            else:
                ip += 3
        elif op == 7:
            a1 = p[ip + 1] if cmd // 100 % 10 == 1 else p[p[ip + 1]]
            a2 = p[ip + 2] if cmd // 1000 % 10 == 1 else p[p[ip + 2]]
            p[p[ip + 3]] = 1 if a1 < a2 else 0
            ip += 4
        elif op == 8:
            a1 = p[ip + 1] if cmd // 100 % 10 == 1 else p[p[ip + 1]]
            a2 = p[ip + 2] if cmd // 1000 % 10 == 1 else p[p[ip + 2]]
            p[p[ip + 3]] = 1 if a1 == a2 else 0
            ip += 4
        elif op == 99:
            break


def part1():
    m = 0
    for x in permutations(range(0, 5)):
        gs = []
        for phase in x:
            g = run(phase)
            next(g)
            g.send(phase)
            gs.append(g)
        signal = 0
        while True:
            for g in gs:
                signal = g.send(signal)
            try:
                for g in gs:
                    next(g)
            except StopIteration:
                break
        m = max(m, signal)
    print(m)


def part2():
    m = 0
    for x in permutations(range(5, 10)):
        gs = []
        for phase in x:
            g = run(phase)
            next(g)
            g.send(phase)
            gs.append(g)
        signal = 0
        while True:
            for g in gs:
                signal = g.send(signal)
            try:
                for g in gs:
                    next(g)
            except StopIteration:
                break
        m = max(m, signal)
    print(m)


part1()
part2()
