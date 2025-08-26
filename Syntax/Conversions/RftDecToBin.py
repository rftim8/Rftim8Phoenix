import os

os.system("cls")


def rft_dec_to_bin():
    a = 255
    b = "255"

    print(f"Dec to bin: {a} -> {bin(a)[2:].zfill(8)}")
    rft_dec_to_bin_format(a)
    rft_string_dec_to_bin_format(b)


def rft_dec_to_bin_format(a):
    print(f"Dec to bin format: {a} -> ", f"{a:08b}")
    print(f"Dec to bin format: {a} -> ", "{0:08b}".format(a))
    print(f"Dec to bin interpolation: {a} -> ", f"{a:010b}"[2:])


def rft_string_dec_to_bin_format(b):
    print(f"String dec to bin format: {b} -> ", f"{int(b):08b}")
    print(f"String dec to bin format: {b} -> ", "{0:08b}".format(int(b)))
    print(f"String dec to bin interpolation: {b} -> ", f"{int(b):010b}"[2:])


rft_dec_to_bin()
