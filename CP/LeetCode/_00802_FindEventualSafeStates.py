# region Imports
from collections import deque
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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00802_FindEventualSafeStates_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_00802_FindEventualSafeStates_Output.txt", "w"
)


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(rft_stl.string_to_2D_list_of_int(input[i]))
        v0.append(rft_stl.string_to_1D_list_of_int(input[i + 1]))


# endregion


# region Solutions
"""
Brute Force
"""


def _00802_FindEventualSafeStates_0(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    safe = [False for _ in range(n)]

    l = []
    r = []

    for i in range(n):
        l.append(set())
        r.append(set())

    q = deque()

    for i in range(n):
        if len(graph[i]) == 0:
            q.append(i)

        for j in graph[i]:
            l[i].add(j)
            r[j].add(i)

    while q:
        j = q.popleft()
        safe[j] = True
        for i in r[j]:
            l[i].remove(j)

            if not l[i]:
                q.append(i)

    x = []

    for i in range(n):
        if safe[i]:
            x.append(i)

    return x


"""
Speed
"""


def _00802_FindEventualSafeStates_1(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    safe = [False] * n
    visited = [False] * n
    inPath = [False] * n

    def dfs(node: int) -> bool:
        if visited[node]:
            return not inPath[node]

        visited[node] = True
        inPath[node] = True

        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False

        inPath[node] = False
        safe[node] = True
        return True

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return [i for i in range(n) if safe[i]]


"""
DFS
"""


def dfs(graph, cur_node, visited, path_visited, safe_nodes):
    visited[cur_node] = True
    path_visited[cur_node] = True

    for neighbor in graph[cur_node]:
        if not visited[neighbor]:
            if dfs(graph, neighbor, visited, path_visited, safe_nodes):
                return True
        elif path_visited[neighbor]:
            return True

    path_visited[cur_node] = False
    safe_nodes.add(cur_node)

    return False


def _00802_FindEventualSafeStates_2(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    visited = [False] * n
    path_visited = [False] * n
    safe_nodes = set()

    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited, path_visited, safe_nodes)

    return sorted(safe_nodes)


def solve():
    for i in range(ncases):
        res0 = _00802_FindEventualSafeStates_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _00802_FindEventualSafeStates_1(v[i])
        output.writelines(str(res1) + "\n")

        res2 = _00802_FindEventualSafeStates_2(v[i])
        output.writelines(str(res2) + "\n")


# endregion


# region Problem Description
"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1. 
The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer 
array of nodes adjacent to node i, meaning there is an edge from node i to each node 
in graph[i].
A node is a terminal node if there are no outgoing edges. 
A node is a safe node if every possible path starting from that node leads to a terminal 
node (or another safe node).
Return an array containing all the safe nodes of the graph. 
The answer should be sorted in ascending order.

Constraints:

n == graph.length
1 <= n <= 104
0 <= graph[i].length <= n
0 <= graph[i][j] <= n - 1
graph[i] is sorted in a strictly increasing order.
The graph may contain self-loops.
The number of edges in the graph will be in the range [1, 4 * 10^4].
"""


def _00802_FindEventualSafeStates():
    os.system("cls")
    data_collector()
    solve()


_00802_FindEventualSafeStates()
# endregion


# region Unit Testing
class _00802_FindEventualSafeStates_Test(unittest.TestCase):
    def test_00802_FindEventualSafeStates_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00802_FindEventualSafeStates_0(v[i]),
                v0[i],
            )

    def test_00802_FindEventualSafeStates_1(self):
        for i in range(ncases):
            self.assertEqual(
                _00802_FindEventualSafeStates_1(v[i]),
                v0[i],
            )

    def test_00802_FindEventualSafeStates_2(self):
        for i in range(ncases):
            self.assertEqual(
                _00802_FindEventualSafeStates_2(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
