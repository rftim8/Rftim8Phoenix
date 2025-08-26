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
    open(f"{cwd}/Data/CP/LeetCode/IO/_02928_DistributeCandiesAmongChildrenI_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02928_DistributeCandiesAmongChildrenI_Output.txt", "w"
)


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []
v1 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(int(input[i]))
        v0.append(int(input[i + 1]))
        v1.append(int(input[i + 2]))


# endregion


# region Solutions
"""
"""


def _02928_DistributeCandiesAmongChildrenI_0(n: int, limit: int) -> int:
    res = 0

    for i in range(limit + 1):
        for j in range(limit + 1):
            k = n - i - j
            if k >= 0 and k <= limit:
                res += 1

    return res


"""
"""


def _02928_DistributeCandiesAmongChildrenI_1(n: int, limit: int) -> int:
    if n > 3 * limit:
        return 0

    comb = lambda x: x * (x - 1) // 2
    result = comb(n + 2)

    if n > limit:
        result -= 3 * comb(n - limit + 1)

    if n - 2 >= 2 * limit:
        result += 3 * comb(n - 2 * limit)

    return result


def solve():
    for i in range(ncases):
        res0 = _02928_DistributeCandiesAmongChildrenI_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")

        res1 = _02928_DistributeCandiesAmongChildrenI_1(v[i], v0[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
You are given two positive integers n and limit.
Return the total number of ways to distribute n candies among 3 children such that no child gets more 
than limit candies.

Constraints:

1 <= n <= 50
1 <= limit <= 50
"""


def _02928_DistributeCandiesAmongChildrenI():
    os.system("cls")
    data_collector()
    solve()


_02928_DistributeCandiesAmongChildrenI()
# endregion


# region Unit Testing
class _02928_DistributeCandiesAmongChildrenI_Test(unittest.TestCase):
    def test_02928_DistributeCandiesAmongChildrenI_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02928_DistributeCandiesAmongChildrenI_0(v[i], v0[i]),
                v1[i],
            )

    def test_02928_DistributeCandiesAmongChildrenI_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02928_DistributeCandiesAmongChildrenI_1(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
