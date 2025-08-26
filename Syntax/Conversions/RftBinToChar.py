import os

os.system("cls")


def rft_bin_to_char():
    a = "01001000"
    b = 1001000

    rft_binary_string_to_char(a)
    rft_binary_int_to_char(b)


def rft_binary_string_to_char(a):
    print(f"Binary string to char: {a} -> {chr(int(a, 2))}")


def rft_binary_int_to_char(b):
    print(f"Binary int to char: {b} -> {chr(int(str(b), 2))}")


rft_bin_to_char()
