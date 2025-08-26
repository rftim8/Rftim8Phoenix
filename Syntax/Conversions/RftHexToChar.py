import os

os.system("cls")


def rft_hex_to_char():
    a = "61"
    b = "576164"

    print(f"Hex to char: {a} -> {chr(int(a, 16))}")
    rft_hex_string_to_string(b)


def rft_hex_string_to_string(b):
    print(f"Hex string to string: {b} -> {bytes.fromhex(b).decode('utf-8')}")


rft_hex_to_char()
