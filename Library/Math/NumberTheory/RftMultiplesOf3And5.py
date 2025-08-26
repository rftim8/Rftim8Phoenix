import os


os.system("cls")


def rft_multiples_of_three_and_five():
    a = [2, 10, 100]
    for i in range(len(a)):
        b = a[i]
        print(int(mul(3, b) + mul(5, b) - mul(15, b)))


def mul(x, nr):
    z = (nr - 1) // x
    return (x + z * x) * z // 2
