# region Imports
from collections import defaultdict, deque
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
    open(f"{cwd}/Data/CP/LeetCode/IO/_01462_CourseScheduleIV_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(f"{cwd}/Data/CP/LeetCode/IO/_01462_CourseScheduleIV_Output.txt", "w")


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []
v1 = []
v2 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(int(input[i]))
        v0.append(rft_stl.string_to_2D_list_of_int(input[i + 1]))
        v1.append(rft_stl.string_to_2D_list_of_int(input[i + 2]))
        v2.append(rft_stl.string_to_1D_list_of_bool(input[i + 3]))


# endregion


# region Solutions
"""
Tree Traversal - On Demand
"""


def _01462_CourseScheduleIV_0(
    numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
) -> List[bool]:
    def isPrerequisite(
        adjList: dict, visited: List[bool], src: int, target: int
    ) -> bool:
        visited[src] = True

        if src == target:
            return True

        for adj in adjList.get(src, []):
            if not visited[adj]:
                if isPrerequisite(adjList, visited, adj, target):
                    return True
        return False

    adjList = {i: [] for i in range(numCourses)}

    for edge in prerequisites:
        adjList[edge[0]].append(edge[1])

    result = []

    for query in queries:
        visited = [False] * numCourses
        result.append(isPrerequisite(adjList, visited, query[0], query[1]))

    return result


"""
Tree Traversal - Preprocessed
"""


def _01462_CourseScheduleIV_1(
    numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
) -> List[bool]:
    def preprocess(
        numCourses: int,
        prerequisites: List[List[int]],
        adjList: dict[int, List[int]],
        isPrerequisite: List[List[bool]],
    ) -> None:
        for i in range(numCourses):
            q = deque([i])

            while q:
                node = q.popleft()

                for adj in adjList.get(node, []):
                    if not isPrerequisite[i][adj]:
                        isPrerequisite[i][adj] = True
                        q.append(adj)

    adjList = {}
    for edge in prerequisites:
        if edge[0] not in adjList:
            adjList[edge[0]] = []
        adjList[edge[0]].append(edge[1])

    isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
    preprocess(numCourses, prerequisites, adjList, isPrerequisite)

    answer = []
    for query in queries:
        answer.append(isPrerequisite[query[0]][query[1]])

    return answer


"""
Topological Sort - Kahn's Algorithm
"""


def _01462_CourseScheduleIV_2(
    numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
) -> List[bool]:
    adjList = defaultdict(list)
    indegree = [0] * numCourses

    for edge in prerequisites:
        adjList[edge[0]].append(edge[1])
        indegree[edge[1]] += 1

    q = deque()

    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)

    nodePrerequisites = defaultdict(set)

    while q:
        node = q.popleft()

        for adj in adjList[node]:
            nodePrerequisites[adj].add(node)

            for prereq in nodePrerequisites[node]:
                nodePrerequisites[adj].add(prereq)

            indegree[adj] -= 1

            if indegree[adj] == 0:
                q.append(adj)

    answer = []

    for q in queries:
        answer.append(q[0] in nodePrerequisites[q[1]])

    return answer


"""
Floyd-Warshall Algorithm
"""


def _01462_CourseScheduleIV_3(
    numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
) -> List[bool]:
    isPrerequisite = [[False] * numCourses for _ in range(numCourses)]

    for edge in prerequisites:
        isPrerequisite[edge[0]][edge[1]] = True

    for intermediate in range(numCourses):
        for src in range(numCourses):
            for target in range(numCourses):
                isPrerequisite[src][target] = isPrerequisite[src][target] or (
                    isPrerequisite[src][intermediate]
                    and isPrerequisite[intermediate][target]
                )

    answer = []

    for query in queries:
        answer.append(isPrerequisite[query[0]][query[1]])

    return answer


"""
Speed - DFS
"""


def _01462_CourseScheduleIV_4(
    numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
) -> List[bool]:
    graph = defaultdict(list)

    for prereq, postreq in prerequisites:
        graph[prereq].append(postreq)

    postreq_set = [set() for _ in range(numCourses)]

    def dfs(course):
        for postreq in graph[course]:
            if postreq not in postreq_set[course]:
                postreq_set[course].add(postreq)
                postreq_set[course].update(dfs(postreq))
        return postreq_set[course]

    for i in range(numCourses):
        dfs(i)

    res = []

    for prereq, postreq in queries:
        if postreq not in postreq_set[prereq]:
            res.append(False)
        else:
            res.append(True)

    return res


def solve():
    for i in range(ncases):
        res0 = _01462_CourseScheduleIV_0(v[i], v0[i], v1[i])
        output.writelines(str(res0) + "\n")

        res1 = _01462_CourseScheduleIV_1(v[i], v0[i], v1[i])
        output.writelines(str(res1) + "\n")

        res2 = _01462_CourseScheduleIV_2(v[i], v0[i], v1[i])
        output.writelines(str(res2) + "\n")

        res3 = _01462_CourseScheduleIV_3(v[i], v0[i], v1[i])
        output.writelines(str(res3) + "\n")

        res4 = _01462_CourseScheduleIV_4(v[i], v0[i], v1[i])
        output.writelines(str(res4) + "\n")


# endregion


# region Problem Description
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
take course ai first if you want to take course bi.
For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. 
If course a is a prerequisite of course b, and course b is a prerequisite of course c, 
then course a is a prerequisite of course c.
You are also given an array queries where queries[j] = [uj, vj]. 
For the jth query, you should answer whether course uj is a prerequisite of course vj or not.
Return a boolean array answer, where answer[j] is the answer to the jth query.

Constraints:

2 <= numCourses <= 100
0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
prerequisites[i].length == 2
0 <= ai, bi <= numCourses - 1
ai != bi
All the pairs [ai, bi] are unique.
The prerequisites graph has no cycles.
1 <= queries.length <= 10^4
0 <= ui, vi <= numCourses - 1
ui != vi
"""


def _01462_CourseScheduleIV():
    os.system("cls")
    data_collector()
    solve()


_01462_CourseScheduleIV()
# endregion


# region Unit Testing
class _01462_CourseScheduleIV_Test(unittest.TestCase):
    def test_01462_CourseScheduleIV_0(self):
        for i in range(ncases):
            self.assertEqual(
                _01462_CourseScheduleIV_0(v[i], v0[i], v1[i]),
                v2[i],
            )

    def test_01462_CourseScheduleIV_1(self):
        for i in range(ncases):
            self.assertEqual(
                _01462_CourseScheduleIV_1(v[i], v0[i], v1[i]),
                v2[i],
            )

    def test_01462_CourseScheduleIV_2(self):
        for i in range(ncases):
            self.assertEqual(
                _01462_CourseScheduleIV_2(v[i], v0[i], v1[i]),
                v2[i],
            )

    def test_01462_CourseScheduleIV_3(self):
        for i in range(ncases):
            self.assertEqual(
                _01462_CourseScheduleIV_3(v[i], v0[i], v1[i]),
                v2[i],
            )

    def test_01462_CourseScheduleIV_4(self):
        for i in range(ncases):
            self.assertEqual(
                _01462_CourseScheduleIV_4(v[i], v0[i], v1[i]),
                v2[i],
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
