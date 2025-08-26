import os

os.system("cls")


def rft_primes():
    a = [ord(i) for i in "abcdefg"]
    rft_string_primes(a)


def rft_string_primes(a):
    print(sum(a))

    x = ""
    for i in range(len(a)):
        if sum(a) % a[i] == 0:
            x = chr(a[i])
            print(a[i])

    print(x)


rft_primes()
