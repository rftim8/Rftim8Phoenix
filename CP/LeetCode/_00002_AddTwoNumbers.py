# region Imports
import os
from typing import List, Optional
import unittest
import sys

cwd = os.getcwd()
sys.path.append(cwd)
import rft_stl
from rft_stl import ListNode

# endregion


# region Data Gethering
input = (
    open(f"{cwd}/Data/CP/LeetCode/IO/_00002_AddTwoNumbers_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_00002_AddTwoNumbers_Output.txt", "w")


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []
v1 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(
            rft_stl.list_of_int_to_listnode(rft_stl.string_to_1D_list_of_int(input[i]))
        )
        v0.append(
            rft_stl.list_of_int_to_listnode(
                rft_stl.string_to_1D_list_of_int(input[i + 1])
            )
        )
        v1.append(rft_stl.string_to_1D_list_of_int(input[i + 2]))


# endregion


# region Solutions
"""
Elementary Math
"""


def _00002_AddTwoNumbers_0(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    head = ListNode(0)
    prev = head
    carry = 0

    while l1 != None or l2 != None or carry != 0:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0
        columnSum = l1Val + l2Val + carry
        carry = columnSum // 10
        newNode = ListNode(columnSum % 10)
        prev.next = newNode
        prev = newNode
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return head.next


def solve():
    for i in range(ncases):
        res0 = _00002_AddTwoNumbers_0(v[i], v0[i])
        output.writelines(str(i) + " " for i in rft_stl.listnode_to_list_of_int(res0))
        output.write("\n")


# endregion


# region Problem Description
"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


def _00002_AddTwoNumbers():
    os.system("cls")
    data_collector()
    solve()


_00002_AddTwoNumbers()
# endregion


# region Unit Testing
class _00002_AddTwoNumbers_Test(unittest.TestCase):
    def test_00002_AddTwoNumbers_0(self):
        for i in range(ncases):
            self.assertEqual(
                rft_stl.listnode_to_list_of_int(_00002_AddTwoNumbers_0(v[i], v0[i])),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
