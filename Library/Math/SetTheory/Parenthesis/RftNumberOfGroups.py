import os

os.system("cls")


def rft_number_of_groups():
    a = "(()()((())))"

    rft_number_of_groups_of_parenthesis(a)


def rft_number_of_groups_of_parenthesis(a):
    a1 = 0
    b1 = 0
    for i in a:
        a1 += [-1, 1][i == "("]
        if a1 > b1:
            b1 = a1

    print(f"Groups of (): {b1}")


rft_number_of_groups()
