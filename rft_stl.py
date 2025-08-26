from collections import deque
from copy import deepcopy
from typing import List


def string_to_1D_list_of_int(s: str) -> List[int]:
    if s == "[]":
        return []
    res = [int(i) for i in s[1:-1].split(",")]
    return res


def string_to_1D_list_of_string(s: str) -> List[str]:
    if s == "[]":
        return []
    res = s[1:-1].replace('"', "").split(",")
    return res


def string_to_1D_list_of_bool(s: str) -> List[bool]:
    if s == "[]":
        return []
    a = s[1:-1].replace('"', "").split(",")
    res = []
    for i in a:
        if i == "true":
            res.append(True)
        else:
            res.append(False)

    return res


def string_to_2D_list_of_int(s: str) -> List[List[int]]:
    if s == "[]":
        return []
    a = [i.replace("[", "").replace("]", "") for i in s.split("],")]
    b = [i.split(",") for i in a]
    res = []
    for i in b:
        if len(i) == 1 and i[0] == "":
            res.append([])
        else:
            res.append(list(map(int, i)))
    return res


def string_to_2D_list_of_string(s: str) -> List[List[str]]:
    if s == "[]":
        return []
    s = s.replace('"', "")
    a = [i.replace("[", "").replace("]", "") for i in s.split("],")]
    res = [i.split(",") for i in a]
    return res


# region ListNode
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def list_of_int_to_listnode(root: List[int]) -> ListNode:
    v = deepcopy(root)
    if v.count == 0:
        return None

    ln = ListNode(v[0])
    head = ln
    for i in range(1, len(v)):
        head.next = ListNode(v[i])
        head = head.next

    return ln


def listnode_to_list_of_int(root: ListNode) -> List[int]:
    ln = deepcopy(root)
    if ln is not None:
        res = []
        head = ln
        prev = head
        while prev is not None:
            res.append(prev.val)
            prev = prev.next
        return res

    return []


def print_list_node(root: ListNode):
    ln = deepcopy(root)
    if ln:
        head = ln
        while head is not None:
            print(head.val, end=" ")
            head = head.next
        print()


# endregion


# region TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_node_from_list_of_int(root: List[int]) -> TreeNode:
    v = deepcopy(root)
    if v == None or len(v) == 0:
        return None

    queue = deque()
    root = TreeNode(v[0])
    queue.append(root)

    for i in range(1, len(v), 2):
        node = queue.popleft()

        if v[i] != -1:
            node.left = TreeNode(v[i])
            queue.append(node.left)

        if i + 1 < len(v) and v[i + 1] != -1:
            node.right = TreeNode(v[i + 1])
            queue.append(node.right)

    return root


def print_binary_tree_in_pre_order(root: TreeNode):
    tn = deepcopy(root)
    if tn:
        v = []
        st = deque()
        st.append(tn)

        while st:
            node = st.pop()

            if node is not None:
                v.append(node.val)
                st.append(node.right)
                st.append(node.left)
        print(v)


def list_of_int_from_binary_tree_in_pre_order(root: TreeNode):
    tn = deepcopy(root)
    if tn:
        v = []
        st = deque()
        st.append(tn)

        while st:
            node = st.pop()

            if node is not None:
                v.append(node.val)
                st.append(node.right)
                st.append(node.left)
        return v
    return []


def print_binary_tree_in_order(root: TreeNode):
    tn = deepcopy(root)
    if tn:
        v = []
        st = deque()
        node = tn

        while node or st:
            while node:
                st.append(node)
                node = node.left

            node = st.pop()
            v.append(node.val)
            node = node.right

        print(v)


def list_of_int_from_binary_tree_in_order(root: TreeNode):
    tn = deepcopy(root)
    if tn:
        v = []
        st = deque()
        node = tn

        while node or st:
            while node:
                st.append(node)
                node = node.left

            node = st.pop()
            v.append(node.val)
            node = node.right

        return v
    return []


def print_binary_tree_in_post_order(root: TreeNode):
    tn = deepcopy(root)
    if tn:
        v = []
        st = deque()
        st.append(tn)

        while st:
            node = st.pop()

            v.append(node.val)

            if node.left:
                st.append(node.left)

            if node.right:
                st.append(node.right)

        sorted(v, reverse=True)
        print(v)


def list_of_int_from_binary_tree_in_post_order(root: TreeNode):
    tn = deepcopy(root)
    if tn:
        v = []
        st = deque()
        st.append(tn)

        while st:
            node = st.pop()

            v.append(node.val)

            if node.left:
                st.append(node.left)

            if node.right:
                st.append(node.right)

        sorted(v, reverse=True)
        return v
    return []


def print_binary_tree_in_level_order(root: TreeNode):
    tn = deepcopy(root)
    if tn:
        q = deque()
        q.append(tn)

        v = []
        while q:
            n = q.count()
            v0 = []

            while n != 0:
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                v0.append(node.val)
                n -= 1

            v.append(v0)

        print(v)


def list_2D_of_int_from_binary_tree_in_level_order(root: TreeNode):
    tn = deepcopy(root)
    if tn:
        q = deque()
        q.append(tn)

        v = []
        while q:
            n = q.count()
            v0 = []

            while n != 0:
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                v0.append(node.val)
                n -= 1

            v.append(v0)

        return v
    return v


# endregion
