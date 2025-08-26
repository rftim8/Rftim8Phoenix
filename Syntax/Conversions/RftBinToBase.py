import os

os.system("cls")


def rft_bin_to_base():
    a = "1001000"

    rft_binary_string_to_base(a, 16)


def rft_binary_string_to_base(a, base):
    print(f"Binary string to base {base}: {a} -> {int(str(int(a, 2)), base)}")


rft_bin_to_base()
