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
    open(
        f"{cwd}/Data/CP/LeetCode/IO/_02960_CountTestedDevicesAfterTestOperations_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02960_CountTestedDevicesAfterTestOperations_Output.txt",
    "w",
)


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(rft_stl.string_to_1D_list_of_int(input[i]))
        v0.append(int(input[i + 1]))


# endregion


# region Solutions
"""
"""


def _02960_CountTestedDevicesAfterTestOperations_0(
    batteryPercentages: List[int],
) -> int:
    res = 0
    c = 0
    for i in batteryPercentages:
        if i - c > 0:
            res += 1
            c += 1

    return res


def solve():
    for i in range(ncases):
        res0 = _02960_CountTestedDevicesAfterTestOperations_0(v[i])
        output.writelines(str(res0) + "\n")


# endregion


# region Problem Description
"""
You are given a 0-indexed integer array batteryPercentages having length n, 
denoting the battery percentages of n 0-indexed devices.
Your task is to test each device i in order from 0 to n - 1, by performing the following test operations:
If batteryPercentages[i] is greater than 0:
Increment the count of tested devices.
Decrease the battery percentage of all devices with indices j in the range [i + 1, n - 1] by 1, 
ensuring their battery percentage never goes below 0, i.e, 
batteryPercentages[j] = max(0, batteryPercentages[j] - 1).
Move to the next device.
Otherwise, move to the next device without performing any test.
Return an integer denoting the number of devices that will be tested after performing the test operations in order.

Constraints:

1 <= n == batteryPercentages.length <= 100 
0 <= batteryPercentages[i] <= 100
"""


def _02960_CountTestedDevicesAfterTestOperations():
    os.system("cls")
    data_collector()
    solve()


_02960_CountTestedDevicesAfterTestOperations()
# endregion


# region Unit Testing
class _02960_CountTestedDevicesAfterTestOperations_Test(unittest.TestCase):
    def test_02960_CountTestedDevicesAfterTestOperations_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02960_CountTestedDevicesAfterTestOperations_0(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
