# region Imports
from collections import deque
from copy import deepcopy
import os
from typing import List
import unittest
import sys

cwd = os.getcwd()
sys.path.append(cwd)
import rft_stl
from rft_stl import ListNode

# endregion


# region Data Gethering
input = (
    open(f"{cwd}/Data/CP/LeetCode/IO/_01669_MergeInBetweenLinkedLists_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_01669_MergeInBetweenLinkedLists_Output.txt", "w"
)


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []
v1 = []
v2 = []
v3 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(
            rft_stl.list_of_int_to_listnode(rft_stl.string_to_1D_list_of_int(input[i]))
        )
        v0.append(int(input[i + 1]))
        v1.append(int(input[i + 2]))
        v2.append(
            rft_stl.list_of_int_to_listnode(
                rft_stl.string_to_1D_list_of_int(input[i + 3])
            )
        )
        v3.append(
            rft_stl.list_of_int_to_listnode(
                rft_stl.string_to_1D_list_of_int(input[i + 4])
            )
        )


# endregion


# region Solutions
"""
"""


def _01669_MergeInBetweenLinkedLists_0(
    l1: ListNode, a: int, b: int, l2: ListNode
) -> ListNode:
    list1 = deepcopy(l1)
    list2 = deepcopy(l2)
    q = deque()
    i = 0
    f = True
    while list1 is not None:
        if i < a or i > b:
            q.append(list1)
        else:
            if f:
                while list2 is not None:
                    q.append(list2)
                    list2 = list2.next
                f = False
        list1 = list1.next
        i += 1

    res = q.popleft()
    n = res
    while len(q) != 0:
        n.next = q.popleft()
        n = n.next

    return res


def solve():
    for i in range(ncases):
        res0 = _01669_MergeInBetweenLinkedLists_0(v[i], v0[i], v1[i], v2[i])
        a = rft_stl.listnode_to_list_of_int(res0)
        output.writelines(str(j) + " " for j in a)
        output.write("\n")


# endregion


# region Problem Description
"""
You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
The blue edges and nodes in the following figure indicate the result:
Build the result list and return its head.

Constraints:

3 <= list1.length <= 10^4
1 <= a <= b < list1.length - 1
1 <= list2.length <= 10^4
"""


def _01669_MergeInBetweenLinkedLists():
    os.system("cls")
    data_collector()
    solve()


_01669_MergeInBetweenLinkedLists()
# endregion


# region Unit Testing
class _01669_MergeInBetweenLinkedLists_Test(unittest.TestCase):
    def test_01669_MergeInBetweenLinkedLists_0(self):
        for i in range(ncases):
            actual = rft_stl.listnode_to_list_of_int(
                _01669_MergeInBetweenLinkedLists_0(v[i], v0[i], v1[i], v2[i])
            )
            expected = rft_stl.listnode_to_list_of_int(v3[i])
            self.assertEqual(
                actual,
                expected,
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
