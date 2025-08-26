import os

os.system("cls")


def rft_hex_to_bin():
    a = "a5"
    b = "0xa5"

    print(f"Hex to bin: {a} -> {bin(int(a, 16))[2:].zfill(8)}")
    print(f"Hex to bin format: {a} -> {format(int(a, 16), 'b')}")
    print(f"Hex to bin format: {b} -> {format(int(b, 16), 'b')}")


rft_hex_to_bin()
