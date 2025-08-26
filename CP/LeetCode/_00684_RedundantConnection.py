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
    open(f"{cwd}/Data/CP/LeetCode/IO/_00684_RedundantConnection_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_00684_RedundantConnection_Output.txt", "w")


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
DFS - Brute Force
"""


def _00684_RedundantConnection_0(edges: List[List[int]]) -> List[int]:
    N = len(edges)
    adj_list = [[] for _ in range(N)]

    def _is_connected(src, target, visited, adj_list):
        visited[src] = True

        if src == target:
            return True

        is_found = False

        for adj in adj_list[src]:
            if not visited[adj]:
                is_found = is_found or _is_connected(adj, target, visited, adj_list)

        return is_found

    for edge in edges:
        visited = [False] * N

        if _is_connected(edge[0] - 1, edge[1] - 1, visited, adj_list):
            return edge

        adj_list[edge[0] - 1].append(edge[1] - 1)
        adj_list[edge[1] - 1].append(edge[0] - 1)

    return []


"""
DFS - Single Traversal
"""


def _00684_RedundantConnection_1(edges: List[List[int]]) -> List[int]:
    cycle_start = -1

    def _DFS(src, visited, adj_list, parent):
        nonlocal cycle_start
        visited[src] = True

        for adj in adj_list[src]:
            if not visited[adj]:
                parent[adj] = src
                _DFS(adj, visited, adj_list, parent)
            elif adj != parent[src] and cycle_start == -1:
                cycle_start = adj
                parent[adj] = src

    N = len(edges)
    visited = [False] * N
    parent = [-1] * N
    adj_list = [[] for _ in range(N)]

    for edge in edges:
        adj_list[edge[0] - 1].append(edge[1] - 1)
        adj_list[edge[1] - 1].append(edge[0] - 1)

    _DFS(0, visited, adj_list, parent)

    cycle_nodes = {}
    node = cycle_start

    while True:
        cycle_nodes[node] = 1
        node = parent[node]
        if node == cycle_start:
            break

    for i in range(len(edges) - 1, -1, -1):
        if (edges[i][0] - 1) in cycle_nodes and (edges[i][1] - 1) in cycle_nodes:
            return edges[i]

    return []


"""
Disjoint Set Union
"""


def _00684_RedundantConnection_2(edges: List[List[int]]) -> List[int]:
    class DSU:
        def __init__(self, N):
            self.N = N
            self.size = [1] * N
            self.representative = list(range(N))

        def _find(self, node):
            if self.representative[node] == node:
                return node

            self.representative[node] = self._find(self.representative[node])

            return self.representative[node]

        def _do_union(self, nodeOne, nodeTwo):
            nodeOne = self._find(nodeOne)
            nodeTwo = self._find(nodeTwo)

            if nodeOne == nodeTwo:
                return False
            else:
                if self.size[nodeOne] > self.size[nodeTwo]:
                    self.representative[nodeTwo] = nodeOne
                    self.size[nodeOne] += self.size[nodeTwo]
                else:
                    self.representative[nodeOne] = nodeTwo
                    self.size[nodeTwo] += self.size[nodeOne]
                return True

    N = len(edges)
    dsu = DSU(N)

    for edge in edges:
        if not dsu._do_union(edge[0] - 1, edge[1] - 1):
            return edge

    return []


"""
Speed
"""


def _00684_RedundantConnection_3(edges: List[List[int]]) -> List[int]:
    par = [i for i in range(len(edges) + 1)]
    rank = [1] * (len(edges) + 1)

    def find(n):
        if n != par[n]:
            par[n] = find(par[n])

        return par[n]

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False

        if rank[p1] >= rank[p2]:
            par[p2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            rank[p2] += rank[p1]
        return True

    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]


def solve():
    for i in range(ncases):
        res0 = _00684_RedundantConnection_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _00684_RedundantConnection_1(v[i])
        output.writelines(str(res1) + "\n")

        res2 = _00684_RedundantConnection_2(v[i])
        output.writelines(str(res2) + "\n")

        res3 = _00684_RedundantConnection_3(v[i])
        output.writelines(str(res3) + "\n")


# endregion


# region Problem Description
"""
In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, 
with one additional edge added. 
The added edge has two different vertices chosen from 1 to n, and was not an edge 
that already existed. 
The graph is represented as an array edges of length n where edges[i] = [ai, bi] 
indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
If there are multiple answers, return the answer that occurs last in the input.

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""


def _00684_RedundantConnection():
    os.system("cls")
    data_collector()
    solve()


_00684_RedundantConnection()
# endregion


# region Unit Testing
class _00684_RedundantConnection_Test(unittest.TestCase):
    def test_00684_RedundantConnection_0(self):
        for i in range(ncases):
            self.assertEqual(
                _00684_RedundantConnection_0(v[i]),
                v0[i],
            )

    def test_00684_RedundantConnection_1(self):
        for i in range(ncases):
            self.assertEqual(
                _00684_RedundantConnection_1(v[i]),
                v0[i],
            )

    def test_00684_RedundantConnection_2(self):
        for i in range(ncases):
            self.assertEqual(
                _00684_RedundantConnection_2(v[i]),
                v0[i],
            )

    def test_00684_RedundantConnection_3(self):
        for i in range(ncases):
            self.assertEqual(
                _00684_RedundantConnection_3(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
