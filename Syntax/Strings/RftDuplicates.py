import os

os.system("cls")


def rft_duplicates():
    a = "122333444455555"

    rft_remove_duplicates(a)


def rft_remove_duplicates(a):
    x = ""
    prev = ""
    for i in a:
        if i != prev:
            x += i
            prev = i

    print(x)


rft_duplicates()
