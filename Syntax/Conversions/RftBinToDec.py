import os

os.system("cls")


def rft_bin_to_dec():
    a = "01001000"
    b = 1001000

    rft_binary_string_to_dec(a)
    rft_binary_int_to_dec(b)


def rft_binary_string_to_dec(a):
    print(f"Binary string to dec: {a} -> {int(a, 2)}")


def rft_binary_int_to_dec(b):
    print(f"Binary int to dec: {b} -> {int(str(b),2)}")


rft_bin_to_dec()
