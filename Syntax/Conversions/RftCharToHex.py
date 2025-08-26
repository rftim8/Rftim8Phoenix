import os

os.system("cls")


def rft_char_to_hex():
    a = "a"
    b = "hello"

    print(f"Char to hex: {a} -> {hex(ord(a))}")
    rft_string_to_hex_array(b)


def rft_string_to_hex_array(b):
    print(f"String to hex: {b} -> {[hex(ord(i)) for i in b]}")


rft_char_to_hex()
