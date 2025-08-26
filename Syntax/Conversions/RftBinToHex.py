import os

os.system("cls")


def rft_bin_to_hex():
    a = "01001000"
    b = 1001000

    rft_binary_string_to_hex(a)
    rft_binary_int_to_hex(b)


def rft_binary_string_to_hex(a):
    print(f"Binary string to hex: {a} -> {hex(int(a,2))}")


def rft_binary_int_to_hex(b):
    print(f"Binary int to hex: {b} -> {hex(int(str(b),2))}")


rft_bin_to_hex()
