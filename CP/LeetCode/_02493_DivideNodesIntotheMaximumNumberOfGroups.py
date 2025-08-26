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
    open(
        f"{cwd}/Data/CP/LeetCode/IO/_02493_DivideNodesIntotheMaximumNumberOfGroups_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02493_DivideNodesIntotheMaximumNumberOfGroups_Output.txt",
    "w",
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
        v0.append(rft_stl.string_to_2D_list_of_int(input[i + 1]))
        v1.append(int(input[i + 2]))


# endregion


# region Solutions
"""
Graph Coloring + Longest Shortest Path
"""


def _is_bipartite(adj_list, node, colors):
    for neighbor in adj_list[node]:
        if colors[neighbor] == colors[node]:
            return False

        if colors[neighbor] != -1:
            continue

        colors[neighbor] = (colors[node] + 1) % 2

        if not _is_bipartite(adj_list, neighbor, colors):
            return False

    return True


def _get_longest_shortest_path(adj_list, src_node, n):
    nodes_queue = deque([src_node])
    visited = [False] * n
    visited[src_node] = True
    distance = 0

    while nodes_queue:
        for _ in range(len(nodes_queue)):
            current_node = nodes_queue.popleft()

            for neighbor in adj_list[current_node]:
                if visited[neighbor]:
                    continue

                visited[neighbor] = True
                nodes_queue.append(neighbor)

        distance += 1

    return distance


def _get_number_of_groups_for_component(adj_list, node, distances, visited):
    max_number_of_groups = distances[node]
    visited[node] = True

    for neighbor in adj_list[node]:
        if visited[neighbor]:
            continue

        max_number_of_groups = max(
            max_number_of_groups,
            _get_number_of_groups_for_component(adj_list, neighbor, distances, visited),
        )

    return max_number_of_groups


def _02493_DivideNodesIntotheMaximumNumberOfGroups_0(
    n: int, edges: List[List[int]]
) -> int:
    adj_list = [[] for _ in range(n)]

    for edge in edges:
        adj_list[edge[0] - 1].append(edge[1] - 1)
        adj_list[edge[1] - 1].append(edge[0] - 1)

    colors = [-1] * n

    for node in range(n):
        if colors[node] != -1:
            continue

        colors[node] = 0

        if not _is_bipartite(adj_list, node, colors):
            return -1

    distances = [_get_longest_shortest_path(adj_list, node, n) for node in range(n)]
    max_number_of_groups = 0
    visited = [False] * n

    for node in range(n):
        if visited[node]:
            continue

        max_number_of_groups += _get_number_of_groups_for_component(
            adj_list, node, distances, visited
        )

    return max_number_of_groups


"""
Graph Coloring + Longest Shortest Path
"""


def _02493_DivideNodesIntotheMaximumNumberOfGroups_1(
    n: int, edges: List[List[int]]
) -> int:
    adj_list = [[] for _ in range(n)]
    parent = [-1] * n
    depth = [0] * n

    def _get_number_of_groups(adj_list, src_node, n):
        nodes_queue = deque()
        layer_seen = [-1] * n
        nodes_queue.append(src_node)
        layer_seen[src_node] = 0
        deepest_layer = 0

        while nodes_queue:
            num_of_nodes_in_layer = len(nodes_queue)

            for _ in range(num_of_nodes_in_layer):
                current_node = nodes_queue.popleft()

                for neighbor in adj_list[current_node]:
                    if layer_seen[neighbor] == -1:
                        layer_seen[neighbor] = deepest_layer + 1
                        nodes_queue.append(neighbor)
                    else:
                        if layer_seen[neighbor] == deepest_layer:
                            return -1
            deepest_layer += 1

        return deepest_layer

    def _find(node, parent):
        while parent[node] != -1:
            node = parent[node]

        return node

    def _union(node1, node2, parent, depth):
        node1 = _find(node1, parent)
        node2 = _find(node2, parent)

        if node1 == node2:
            return

        if depth[node1] < depth[node2]:
            node1, node2 = node2, node1

        parent[node2] = node1

        if depth[node1] == depth[node2]:
            depth[node1] += 1

    for edge in edges:
        adj_list[edge[0] - 1].append(edge[1] - 1)
        adj_list[edge[1] - 1].append(edge[0] - 1)
        _union(edge[0] - 1, edge[1] - 1, parent, depth)

    num_of_groups_for_component = {}

    for node in range(n):
        number_of_groups = _get_number_of_groups(adj_list, node, n)

        if number_of_groups == -1:
            return -1

        root_node = _find(node, parent)
        num_of_groups_for_component[root_node] = max(
            num_of_groups_for_component.get(root_node, 0), number_of_groups
        )

    total_number_of_groups = sum(num_of_groups_for_component.values())

    return total_number_of_groups


def solve():
    for i in range(ncases):
        res0 = _02493_DivideNodesIntotheMaximumNumberOfGroups_0(v[i], v0[i])
        output.writelines(str(res0) + "\n")

        res1 = _02493_DivideNodesIntotheMaximumNumberOfGroups_1(v[i], v0[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
You are given a positive integer n representing the number of nodes in an undirected graph. 
The nodes are labeled from 1 to n.
You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that 
there is a bidirectional edge between nodes ai and bi. 
Notice that the given graph may be disconnected.
Divide the nodes of the graph into m groups (1-indexed) such that:
Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs 
to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. 
Return -1 if it is impossible to group the nodes with the given conditions.

Constraints:

1 <= n <= 500
1 <= edges.length <= 10^4
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
There is at most one edge between any pair of vertices.
"""


def _02493_DivideNodesIntotheMaximumNumberOfGroups():
    os.system("cls")
    data_collector()
    solve()


_02493_DivideNodesIntotheMaximumNumberOfGroups()
# endregion


# region Unit Testing
class _02493_DivideNodesIntotheMaximumNumberOfGroups_Test(unittest.TestCase):
    def test_02493_DivideNodesIntotheMaximumNumberOfGroups_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02493_DivideNodesIntotheMaximumNumberOfGroups_0(v[i], v0[i]),
                v1[i],
            )

    def test_02493_DivideNodesIntotheMaximumNumberOfGroups_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02493_DivideNodesIntotheMaximumNumberOfGroups_1(v[i], v0[i]),
                v1[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
