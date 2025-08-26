import os

os.system("cls")


def rft_dec_to_base():
    a = 28

    rft_int_to_base(a, 16)


def rft_int_to_base(a, base):
    print(f"Dec to base {base}: {a} -> {int(str(a),base)}")


rft_dec_to_base()
