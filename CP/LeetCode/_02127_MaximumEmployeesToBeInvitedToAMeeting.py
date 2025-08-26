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
        f"{cwd}/Data/CP/LeetCode/IO/_02127_MaximumEmployeesToBeInvitedToAMeeting_Input.txt"
    )
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_02127_MaximumEmployeesToBeInvitedToAMeeting_Output.txt",
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
Cycle Detection With Extended Paths
"""


def _02127_MaximumEmployeesToBeInvitedToAMeeting_0(favorite: List[int]) -> int:
    def _bfs(
        start_node: int, visited_nodes: set, reversed_graph: List[List[int]]
    ) -> int:
        queue = deque([(start_node, 0)])
        max_distance = 0

        while queue:
            current_node, current_distance = queue.popleft()
            for neighbor in reversed_graph[current_node]:
                if neighbor in visited_nodes:
                    continue

                visited_nodes.add(neighbor)
                queue.append((neighbor, current_distance + 1))
                max_distance = max(max_distance, current_distance + 1)

        return max_distance

    num_people = len(favorite)
    reversed_graph = [[] for _ in range(num_people)]

    for person in range(num_people):
        reversed_graph[favorite[person]].append(person)

    longest_cycle = 0
    two_cycle_invitations = 0
    visited = [False] * num_people

    for person in range(num_people):
        if not visited[person]:
            visited_persons = {}
            current_person = person
            distance = 0

            while True:
                if visited[current_person]:
                    break
                visited[current_person] = True
                visited_persons[current_person] = distance
                distance += 1
                next_person = favorite[current_person]

                if next_person in visited_persons:
                    cycle_length = distance - visited_persons[next_person]
                    longest_cycle = max(longest_cycle, cycle_length)

                    if cycle_length == 2:
                        visited_nodes = {current_person, next_person}
                        two_cycle_invitations += (
                            2
                            + _bfs(next_person, visited_nodes, reversed_graph)
                            + _bfs(
                                current_person,
                                visited_nodes,
                                reversed_graph,
                            )
                        )
                    break
                current_person = next_person

    return max(longest_cycle, two_cycle_invitations)


"""
Topological Sort To Reduce Non-cyclic Nodes
"""


def _02127_MaximumEmployeesToBeInvitedToAMeeting_1(favorite: List[int]) -> int:
    n = len(favorite)
    in_degree = [0] * n

    for person in range(n):
        in_degree[favorite[person]] += 1

    q = deque()

    for person in range(n):
        if in_degree[person] == 0:
            q.append(person)

    depth = [1] * n

    while q:
        current_node = q.popleft()
        next_node = favorite[current_node]
        depth[next_node] = max(depth[next_node], depth[current_node] + 1)
        in_degree[next_node] -= 1

        if in_degree[next_node] == 0:
            q.append(next_node)

    longest_cycle = 0
    two_cycle_invitations = 0

    for person in range(n):
        if in_degree[person] == 0:
            continue

        cycle_length = 0
        current = person

        while in_degree[current] != 0:
            in_degree[current] = 0
            cycle_length += 1
            current = favorite[current]

        if cycle_length == 2:
            two_cycle_invitations += depth[person] + depth[favorite[person]]
        else:
            longest_cycle = max(longest_cycle, cycle_length)

    return max(longest_cycle, two_cycle_invitations)


def solve():
    for i in range(ncases):
        res0 = _02127_MaximumEmployeesToBeInvitedToAMeeting_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _02127_MaximumEmployeesToBeInvitedToAMeeting_1(v[i])
        output.writelines(str(res1) + "\n")


# endregion


# region Problem Description
"""
A company is organizing a meeting and has a list of n employees, waiting to be invited. 
They have arranged for a large circular table, capable of seating any number of employees.
The employees are numbered from 0 to n - 1. 
Each employee has a favorite person and they will attend the meeting only if they can 
sit next to their favorite person at the table. 
The favorite person of an employee is not themself.
Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person 
of the ith employee, return the maximum number of employees that can be invited to the meeting.

Constraints:

n == favorite.length
2 <= n <= 10^5
0 <= favorite[i] <= n - 1
favorite[i] != i
"""


def _02127_MaximumEmployeesToBeInvitedToAMeeting():
    os.system("cls")
    data_collector()
    solve()


_02127_MaximumEmployeesToBeInvitedToAMeeting()
# endregion


# region Unit Testing
class _02127_MaximumEmployeesToBeInvitedToAMeeting_Test(unittest.TestCase):
    def test_02127_MaximumEmployeesToBeInvitedToAMeeting_0(self):
        for i in range(ncases):
            self.assertEqual(
                _02127_MaximumEmployeesToBeInvitedToAMeeting_0(v[i]),
                v0[i],
            )

    def test_02127_MaximumEmployeesToBeInvitedToAMeeting_1(self):
        for i in range(ncases):
            self.assertEqual(
                _02127_MaximumEmployeesToBeInvitedToAMeeting_1(v[i]),
                v0[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
