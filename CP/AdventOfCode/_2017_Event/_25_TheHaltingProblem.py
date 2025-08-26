import os

os.system("cls")
cwd = os.getcwd()

s = (
    open(f"{cwd}/CP/AdventOfCode/_2017_Event/_25_TheHaltingProblem.txt")
    .read()
    .split("\n")
)

steps = (int)(s[1].split(" ")[-2])
print(steps)

a, b, c, d, e, f = range(6)
left, right = 0, 1

tm = {
    (a, 0): (1, right, b),
    (a, 1): (0, left, c),
    (b, 0): (1, left, a),
    (b, 1): (1, right, d),
    (c, 0): (1, right, a),
    (c, 1): (0, left, e),
    (d, 0): (1, right, a),
    (d, 1): (0, right, b),
    (e, 0): (1, left, f),
    (e, 1): (1, left, c),
    (f, 0): (1, right, d),
    (f, 1): (1, right, a),
}

tape = {}
head, state = 0, a

for i in range(steps):
    val = tape.get(head, 0)
    wval, move, nextstate = tm.get((state, val))

    tape[head] = wval
    head = head + 1 if move == right else head - 1
    state = nextstate

print(sum(tape.values()))
