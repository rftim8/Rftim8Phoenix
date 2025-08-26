import os

os.system("cls")


def rft_bitwise():
    a = 10
    b = 3

    rft_shift_right(a, b)
    rft_shift_left(a, b)
    rft_logic_and(a, b)
    rft_logic_or(a, b)
    rft_logic_not(b)
    rft_exclusive_or(a, b)


def rft_shift_right(a, b):
    c = a >> b
    a1 = bin(a).replace("0b", "")
    b1 = bin(b).replace("0b", "")
    c1 = bin(c).replace("0b", "")
    print(f"Shift right: {a} >> {b} ({a1} >> {b1}) = {c} ({c1})")


def rft_shift_left(a, b):
    c = a << b
    a1 = bin(a).replace("0b", "")
    b1 = bin(b).replace("0b", "")
    c1 = bin(c).replace("0b", "")
    print(f"Shift left: {a} << {b} ({a1} << {b1}) = {c} ({c1})")


def rft_logic_and(a, b):
    c = a & b
    a1 = bin(a).replace("0b", "")
    b1 = bin(b).replace("0b", "")
    c1 = bin(c).replace("0b", "")
    print(f"Logic and: {a} & {b} ({a1} & {b1}) = {c} ({c1})")


def rft_logic_or(a, b):
    c = a | b
    a1 = bin(a).replace("0b", "")
    b1 = bin(b).replace("0b", "")
    c1 = bin(c).replace("0b", "")
    print(f"Logic or: {a} | {b} ({a1} | {b1}) = {c} ({c1})")


def rft_logic_not(a):
    c = ~a
    a1 = bin(a).replace("0b", "")
    c1 = bin(c).replace("0b", "")
    print(f"Logic not: ~{a} ({a1}) = {c} ({c1})")


def rft_exclusive_or(a, b):
    c = a ^ b
    a1 = bin(a).replace("0b", "")
    b1 = bin(b).replace("0b", "")
    c1 = bin(c).replace("0b", "")
    print(f"Exclusive or: {a} ^ {b} ({a1} ^ {b1}) = {c} ({c1})")


rft_bitwise()
