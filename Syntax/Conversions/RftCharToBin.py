import os

os.system("cls")


def rft_char_to_bin():
    a = "a"
    b = "hello"

    print(f"Char to bin: {a} -> {bin(ord(a))[2:].zfill(8)}")
    rft_char_to_bin_join(a)
    rft_char_to_bin_map(a)
    rft_string_to_bin(b)
    rft_string_to_bin_array(b)
    rft_string_to_bin_array_format(b)


def rft_char_to_bin_join(a):
    print(f"Char to bin: {a} -> {''.join(format(ord(a), 'b')).zfill(8)}")


def rft_char_to_bin_map(a):
    print(
        f"Char to bin map: {a} -> {''.join(map(bin, bytearray(a, 'utf8')))[2:].zfill(8)}"
    )


def rft_string_to_bin(b):
    print(f"String to bin: {b} -> {' '.join(format(ord(i), 'b').zfill(8) for i in b)}")


def rft_string_to_bin_array(b):
    c = [bin(ord(i))[2:].zfill(8) for i in b]
    print(f"String to bin array: {b} -> {c}")


def rft_string_to_bin_array_format(b):
    c = [format(ord(i), "b").zfill(8) for i in b]
    print(f"String to bin array format: {b} -> {c}")


rft_char_to_bin()
