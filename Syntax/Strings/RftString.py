import os

os.system("cls")


def rft_string():
    a = "a"
    b = "Hello World"
    c = "SDF234ewr"
    d = "1+22+3+4"
    e = "10101010"

    print(f"Loop: {5*a}")
    print(f"All uppercase: {b} -> {[i for i in b if i.isupper()]}")
    print(f"Caseless comparisons: {c} -> {c.casefold()}")
    print(f"Count char 'l' in string: {b.count('l')}")
    print(f"Swapcase: {c} -> {c.swapcase()}")
    rft_sorted_ints_in_string(d)
    rft_negate_binary_string(e)


def rft_sorted_ints_in_string(d):
    print(
        f"Sorted ints in string: {d} -> {' '.join(str(i) for i in sorted(int(i) for i in d.split('+')))}"
    )


def rft_negate_binary_string(e):
    print(f"Negate binary string: {e} -> {''.join(str(1-int(i)) for i in e)}")


rft_string()
