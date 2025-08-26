# region Imports
from collections import deque
import os
from typing import List, Optional
import unittest
import sys

cwd = os.getcwd()
sys.path.append(cwd)
import rft_stl
from rft_stl import TreeNode

# endregion


# region Data Gethering
input = (
    open(f"{cwd}/Data/CP/LeetCode/IO/_00094_BinaryTreeInorderTraversal_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_00094_BinaryTreeInorderTraversal_Output.txt", "w"
)


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        tn = rft_stl.binary_tree_node_from_list_of_int(
            rft_stl.string_to_1D_list_of_int(input[i])
        )
        v.append(tn)
        v0.append(rft_stl.string_to_1D_list_of_int(input[i + 1]))


# endregion


# region Solutions
"""
Iterative
"""


def _00094_BinaryTreeInorderTraversal_0(root: Optional[TreeNode]) -> List[int]:
    res = []
    s = deque()
    c = root

    while c != None or bool(s):
        while c != None:
            s.append(c)
            c = c.left

        c = s.pop()
        if c.val != None:
            res.append(c.val)
        c = c.right

    return res


"""
Recursive
"""


def helper(root, res):
    if root is not None:
        helper(root.left, res)
        res.append(root.val)
        helper(root.right, res)


def _00094_BinaryTreeInorderTraversal_1(root: Optional[TreeNode]) -> List[int]:
    res = []
    helper(root, res)

    return res


def solve():
    for i in range(ncases):
        res0 = _00094_BinaryTreeInorderTraversal_0(v[i])
        if res0:
            output.writelines(str(j) + " " for j in res0)
        output.write("\n")
        res1 = _00094_BinaryTreeInorderTraversal_1(v[i])
        if res1:
            output.writelines(str(j) + " " for j in res1)
        output.write("\n")


"""
Morris
"""


def _00094_BinaryTreeInorderTraversal_2(root: Optional[TreeNode]) -> List[int]:
    res = []
    curr = root

    while curr is not None:
        if curr.left is None:
            res.append(curr.val)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right is not None and pre.right != curr:
                pre = pre.right

            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                res.append(curr.val)
                curr = curr.right

    return res


def solve():
    for i in range(ncases):
        res0 = _00094_BinaryTreeInorderTraversal_0(v[i])
        if res0:
            output.writelines(str(j) + " " for j in res0)
        output.write("\n")

        res1 = _00094_BinaryTreeInorderTraversal_1(v[i])
        if res1:
            output.writelines(str(j) + " " for j in res1)
        output.write("\n")

        res2 = _00094_BinaryTreeInorderTraversal_2(v[i])
        if res2:
            output.writelines(str(j) + " " for j in res2)
        output.write("\n")


# endregion


# region Problem Description
"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


def _00094_BinaryTreeInorderTraversal():
    os.system("cls")
    data_collector()
    solve()


_00094_BinaryTreeInorderTraversal()
# endregion


# region Unit Testing
class _00094_BinaryTreeInorderTraversal_Test(unittest.TestCase):
    def test_00094_BinaryTreeInorderTraversal_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00094_BinaryTreeInorderTraversal_0(v[i]),
                v0[i],
            )

    def test_00094_BinaryTreeInorderTraversal_1(self):
        for i in range(ncases):
            self.assertEqual(
                _00094_BinaryTreeInorderTraversal_1(v[i]),
                v0[i],
            )

    def test_00094_BinaryTreeInorderTraversal_2(self):
        for i in range(ncases):
            self.assertEqual(
                _00094_BinaryTreeInorderTraversal_2(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
