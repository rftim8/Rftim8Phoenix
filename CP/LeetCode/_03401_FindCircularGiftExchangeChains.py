# region Imports
import os
from typing import List
import unittest
import sys

cwd = os.getcwd()
sys.path.append(cwd)
import rft_stl

# endregion


# region Data Gethering
input = (
    open(f"{cwd}/Data/CP/LeetCode/IO/_03401_FindCircularGiftExchangeChains_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_03401_FindCircularGiftExchangeChains_Output.txt", "w"
)


ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []
v1 = []


def data_collector():
    for i in range(2, ncases * nparams, nparams):
        v.append(rft_stl.string_to_1D_list_of_string(input[i]))
        v0.append(rft_stl.string_to_2D_list_of_int(input[i + 1]))
        v1.append(rft_stl.string_to_1D_list_of_int(input[i + 2]))


# endregion


# region Solutions
"""
"""


def _03401_FindCircularGiftExchangeChains_0() -> int:
    res = 0
    
    return res


def solve():
    for i in range(ncases):
        res0 = _03401_FindCircularGiftExchangeChains_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""

"""


def _03401_FindCircularGiftExchangeChains():
    os.system("cls")
    data_collector()
    solve()


_03401_FindCircularGiftExchangeChains()
# endregion


# region Unit Testing
class _03401_FindCircularGiftExchangeChains_Test(unittest.TestCase):
    def test_03401_FindCircularGiftExchangeChains_0(self):
        for i in range(ncases):
            self.assertEqual(
                _03401_FindCircularGiftExchangeChains_0(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
