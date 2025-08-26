import os

os.system("clear")

memo = {}


def get_partitions(n, max):
    if n == 0:
        return 1

    if (n, max) in memo:
        return memo[(n, max)]

    count = 0
    for i in range(min(max, n), 0, -1):
        count += get_partitions(n - i, i - 1)

    memo[(n, max)] = count
    return count


def get_strict_partitions(n):
    return get_partitions(n, n)


n = 500
partitions = get_strict_partitions(n) - 1
print(partitions)
