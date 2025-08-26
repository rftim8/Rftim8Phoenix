import os
import timeit

os.system("cls")

def part_one():
    res = 0

    return res


def part_two():
    res = 0

    return res


#region Default Timer
tic = timeit.default_timer()

print(part_one())
# print(part_two())

toc = timeit.default_timer()
elapsed_time = toc - tic
print(f"Execution time in seconds: {elapsed_time:.6f}")
#endregion

#region Average Timer
elapsed_time = timeit.timeit(part_one, number=1000)
print(f"Average execution time per call: {elapsed_time:.6f} seconds")
#endregion
