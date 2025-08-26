import os

os.system("cls")

a = 12  # Number of eggs!
b = 0
c = 0
d = 0

cwd = os.getcwd()

inf = open(f"{cwd}/CP/AdventOfCode/_2016_Event/_23_SafeCracking.txt")
lines = inf.readlines()
states = [(a, b, c, d, -1) for i in range(len(lines))]

tc = 0
i = 0
while i < len(lines):
    line = lines[i]
    vals = line[4:].split()
    ins = line[:3]
    if ins == "cpy":
        if vals[1] in ("a", "b", "c", "d"):
            exec(vals[1] + "=" + vals[0])
    elif ins == "inc":
        exec(vals[0] + "+= 1")
    elif ins == "dec":
        exec(vals[0] + "-= 1")
    elif ins == "tgl":
        tc += 1
        trg = i + eval(vals[0])
        if trg < len(lines):
            tgli = lines[trg]
            tgv = tgli[4:]
            lv = len(tgv.split())
            tgin = tgli[:3]
            if tgin == "inc":
                tgin = "dec"
            elif lv == 1:
                tgin = "inc"
            elif tgin == "jnz":
                tgin = "cpy"
            elif lv == 2:
                tgin = "jnz"
            else:
                print("this stuff should not happen!")
            lines[trg] = tgin + " " + tgv
    if ins == "jnz" and eval(vals[0]):
        jmp = eval(vals[1])
        if jmp < 0:
            aa, bb, cc, dd, ttc = states[i]
            if tc == ttc:
                x = vals[0]
                try:
                    reps = int(eval(x + "/(" + x + x + "-" + x + ")"))
                    a += (a - aa) * reps
                    b += (b - bb) * reps
                    c += (c - cc) * reps
                    d += (d - dd) * reps
                    jmp = 1
                    states[i] = (a, b, c, d, -1)
                except:
                    print("Not OK jump...", x, eval(x), eval(x + x))
                    states[i] = (a, b, c, d, tc)
            else:
                states[i] = (a, b, c, d, tc)
        i += jmp
    else:
        i += 1

print(a, b, c, d)
print("a contains", a)
