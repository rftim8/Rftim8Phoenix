import heapq
import pathlib
import sys
import os

os.system("cls")
cwd = os.getcwd()

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent / "lib"))

from collections import defaultdict


class Maze:
    @staticmethod
    def _move(pt, d):
        return (pt[0] + d[0], pt[1] + d[1])

    def __init__(self, data):
        self.maze = {}
        self.portals = {}
        self.paths = defaultdict(dict)

        self._parse(data)

    def _parse(self, data):
        rows = data.rstrip("\n").split("\n")
        for y, row in enumerate(rows):
            for x, cell in enumerate(row):
                self.maze[(x, y)] = {"output": cell, "portal": None}

                if not cell.isupper():
                    continue

                portal = None
                outer = None

                if x > 0 and row[x - 1] == ".":
                    portal = cell + row[x + 1]
                    outer = x + 2 == len(row)
                    entry = (x - 1, y)

                elif x + 1 < len(row) and row[x + 1] == ".":
                    portal = row[x - 1] + cell
                    outer = x - 1 == 0
                    entry = (x + 1, y)

                elif y > 0 and rows[y - 1][x] == ".":
                    portal = cell + rows[y + 1][x]
                    outer = y + 2 == len(rows)
                    entry = (x, y - 1)

                elif y + 1 < len(rows) and rows[y + 1][x] == ".":
                    portal = rows[y - 1][x] + cell
                    outer = y - 1 == 0
                    entry = (x, y + 1)

                if portal is not None:
                    self.portals[(outer, portal)] = entry
                    self.maze[(x, y)]["portal"] = (outer, portal)

    def _shortest_path(self, pt1, pt2):
        path_steps = None
        visited = set()
        q = [(0, pt1)]

        while len(q):
            steps, pt = heapq.heappop(q)
            visited.add(pt)

            if pt == pt2:
                path_steps = steps
                break

            for adj in (Maze._move(pt, d) for d in ((0, -1), (1, 0), (0, 1), (-1, 0))):
                if (
                    adj in visited
                    or adj not in self.maze
                    or self.maze[adj]["output"] != "."
                ):
                    continue

                if self.maze[adj]["output"] == ".":
                    heapq.heappush(q, (steps + 1, adj))

        return path_steps

    def _resolve_paths(self):
        for start, start_pt in self.portals.items():
            for end, end_pt in self.portals.items():
                if start == end:
                    continue

                steps = self._shortest_path(self.portals[start], self.portals[end])
                if steps is None:
                    continue

                self.paths[start][end] = (steps, -1 if end[0] else 1)
                self.paths[end][start] = (steps, -1 if start[0] else 1)

        return

    def walk_path(self):
        visited = set()
        q = [(0, self.portals[(True, "AA")])]

        while len(q):
            steps, pt = heapq.heappop(q)
            visited.add(pt)

            if pt == self.portals[(True, "ZZ")]:
                break

            for adj in (Maze._move(pt, d) for d in ((0, -1), (1, 0), (0, 1), (-1, 0))):
                if (
                    adj in visited
                    or adj not in self.maze
                    or self.maze[adj]["output"] == "#"
                ):
                    continue

                if self.maze[adj]["output"] == ".":
                    heapq.heappush(q, (steps + 1, adj))

                elif self.maze[adj]["portal"] is not None:
                    d, portal = self.maze[adj]["portal"]
                    warp = self.portals.get((not d, portal), None)
                    if warp is not None and warp not in visited:
                        heapq.heappush(q, (steps + 1, warp))

        return steps

    def recurse_path(self):
        self._resolve_paths()

        path_steps = None

        visited = set()
        q = [(0, 0, (True, "AA"))]

        while len(q):
            steps, depth, portal = heapq.heappop(q)

            if portal == (False, "ZZ") and depth < 0:
                path_steps = steps - 1
                break

            for hop, (hopsteps, incr) in self.paths[portal].items():
                if depth > 0 and incr < 0 and hop in {(True, "AA"), (True, "ZZ")}:
                    continue

                elif depth == 0 and incr < 0 and hop != (True, "ZZ"):
                    continue

                elif (depth + incr, portal, hop) in visited:
                    continue

                visited.add((depth + incr, portal, hop))
                heapq.heappush(
                    q, (steps + hopsteps + 1, depth + incr, (not hop[0], hop[1]))
                )

        return path_steps


def run():
    input_file = f"{cwd}/CP/AdventOfCode/_2019_Event/_20_DonutMaze.txt"
    lines = open(input_file).read()

    maze = Maze(lines)
    steps = maze.walk_path()
    print(f"Steps from AA to ZZ: {steps}")

    maze = Maze(lines)
    steps = maze.recurse_path()
    print(f"Recursive steps from AA to ZZ: {steps}")


if __name__ == "__main__":
    run()
    sys.exit(0)
