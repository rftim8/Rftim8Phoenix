import os

os.system("cls")


def rft_dec_to_char():
    a = 97
    b = [97, 34, 45, 123, 110]

    print(f"Dec to char: {a} -> {chr(a)}")
    rft_dec_array_to_string(b)


def rft_dec_array_to_string(b):
    print(f"Dec array to string: {b} -> {''.join(chr(i) for i in b)}")


rft_dec_to_char()
