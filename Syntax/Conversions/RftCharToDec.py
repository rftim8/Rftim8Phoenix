import os

os.system("cls")


def rft_char_to_dec():
    a = "a"
    b = "hello"
    c = "123"

    print(f"Char to dec: {a} -> {ord(a)}")
    rft_string_int_to_dec(c)
    rft_string_to_dec(b)
    rft_string_to_dec_string(b)
    rft_string_to_dec_array(b)


def rft_string_int_to_dec(c):
    print(f"String int to dec: {c} -> {int(c)}")


def rft_string_to_dec_string(b):
    print(f"String to dec: {b} -> {' '.join(str(ord(i)) for i in b)}")


def rft_string_to_dec_array(b):
    print(f"String to dec: {b} -> {[ord(i) for i in b]}")


def rft_string_to_dec(b):
    print(f"String to dec: {b} -> {sum([ord(i) for i in b])}")


rft_char_to_dec()
