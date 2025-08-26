import os
from itertools import groupby

os.system("cls")


def _01_not_quite_lisp(iterations, sequence="1113122113"):
    arr = [sequence]

    def get_sequence(arr, iterations, sequence):
        if iterations == 0:
            return arr
        else:
            current = "".join(
                str(len(list(group))) + key for key, group in groupby(sequence)
            )
            arr.append(current)
            get_sequence(arr, iterations - 1, current)
        return arr

    final_sequence = get_sequence(arr, iterations, sequence)
    return final_sequence


print(len(_01_not_quite_lisp(50)[50]))
