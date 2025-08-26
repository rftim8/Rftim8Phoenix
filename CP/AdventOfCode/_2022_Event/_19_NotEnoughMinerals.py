import os
import collections
import time
from heapq import heappop


os.system("cls")
cwd = os.getcwd()


def read_input(
    path: str = f"{cwd}/CP/AdventOfCode/_2022_Event/_19_NotEnoughMinerals.txt",
):
    inputs = []
    with open(path) as filet:
        for idx, line in enumerate(filet.readlines()):
            line = line.rstrip()
            line = line.split(": ")
            blueprint = int(line[0].split(" ")[-1])
            assert blueprint == idx + 1, "Blueprint number is not as expected."
            robots = line[1].split(". ")
            robot_materials = []
            for idx, robot in enumerate(robots):
                robot = robot.split(" ")
                if robot[1] == "ore":
                    assert idx == 0, "The ore robot is not the first."
                    assert robot[5] == "ore", "The ore robot is not as expected."
                    robot_materials.append((int(robot[4]), 0, 0, 0))
                elif robot[1] == "clay":
                    assert idx == 1, "The clay robot is not the second."
                    assert robot[5] == "ore", "The clay robot is not as expected."
                    robot_materials.append((int(robot[4]), 0, 0, 0))
                elif robot[1] == "obsidian":
                    assert idx == 2, "The obsidian robot is not the third."
                    assert (
                        robot[5] == "ore" and robot[8] == "clay"
                    ), "The obsidian robot is not as expected."
                    robot_materials.append((int(robot[4]), int(robot[7]), 0, 0))
                elif robot[1] == "geode":
                    assert idx == 3, "The geode robot is not the fourth."
                    assert (
                        robot[5] == "ore" and robot[8] == "obsidian."
                    ), "The geode robot is not as expected."
                    robot_materials.append((int(robot[4]), 0, int(robot[7]), 0))
            inputs.append(robot_materials)

    return inputs


def optimize_factory(
    costs: list[tuple[int, int, int, int]], time_horizon: int, debug=False
) -> tuple[int, int]:
    max_materials_necessary = [
        max(cost[idx] for cost in costs) for idx in range(len(costs))
    ]
    max_materials_necessary[3] = float("inf")
    queue = collections.deque([(time_horizon, (0, 0, 0, 0), (1, 0, 0, 0))])
    result = 0
    counter = 0
    start_time = time.time()
    state_cache = collections.defaultdict(lambda: -1)
    while queue:
        time_left, materials, robots = queue.pop()
        counter += 1
        if counter % 500_000 == 0 and debug:
            print(time_left, materials, robots, len(queue))
            print(
                f"{counter / 1_000_000:0.1f} M. Result: {result}. Elapsed time: {time.time() - start_time} s."
            )
            print()

        result = max(result, materials[3])
        upper_bound_geodes = (
            ((time_left + robots[3]) * (time_left + robots[3] + 1)) // 2
            - (robots[3] * (robots[3] + 1)) // 2
            + materials[3]
        )

        if upper_bound_geodes <= result:
            continue

        key = (time_left, materials[:3], robots)
        if state_cache[key] >= materials[3]:
            continue
        else:
            state_cache[key] = materials[3]

        if not time_left:
            continue

        should_wait = any(
            material < max_material and robot
            for material, max_material, robot in zip(
                materials, max_materials_necessary, robots
            )
        )

        if should_wait:
            new_materials = tuple(
                material + robot for material, robot in zip(materials, robots)
            )
            new_robots = robots[:]

            queue.append((time_left - 1, new_materials, new_robots))

        for idx, cost in enumerate(costs):
            if max_materials_necessary[idx] > robots[idx] and all(
                material >= prize for material, prize in zip(materials, cost)
            ):
                new_materials = tuple(
                    material + robot - prize
                    for material, robot, prize in zip(materials, robots, cost)
                )
                new_robots = tuple(
                    robot + 1 if rx == idx else robot for rx, robot in enumerate(robots)
                )
                queue.append((time_left - 1, new_materials, new_robots))

    return result, counter


def optimize_factory_heaped(
    costs: list[tuple[int, int, int, int]], time_horizon: int, debug=False
) -> tuple[int, int]:
    max_materials_necessary = [
        max(cost[idx] for cost in costs) for idx in range(len(costs))
    ]
    max_materials_necessary[3] = float("inf")
    queue = [(0, time_horizon, (0, 0, 0, 0), (1, 0, 0, 0))]
    result = 0
    counter = 0
    start_time = time.time()
    state_cache = collections.defaultdict(lambda: -1)
    while queue:
        _, time_left, materials, robots = heappop(queue)
        counter += 1
        if counter % 500_000 == 0 and debug:
            print(time_left, materials, robots, len(queue))
            print(
                f"{counter / 1_000_000:0.1f} M. Result: {result}. Elapsed time: {time.time() - start_time} s."
            )
            print()
        result = max(result, materials[3] + robots[3] * time_left)
        upper_bound_geodes = (
            ((time_left + robots[3]) * (time_left + robots[3] + 1)) // 2
            - (robots[3] * (robots[3] + 1)) // 2
            + materials[3]
        )
        if upper_bound_geodes <= result:
            continue

        key = (time_left, materials[:3], robots)
        if state_cache[key] >= materials[3]:
            continue
        else:
            state_cache[key] = materials[3]

        if not time_left:
            continue

        should_wait = any(
            material < max_material and robot
            for material, max_material, robot in zip(
                materials, max_materials_necessary, robots
            )
        )

        if should_wait:
            new_materials = tuple(
                material + robot for material, robot in zip(materials, robots)
            )
            new_robots = robots[:]
            queue.append((-new_robots[3], time_left - 1, new_materials, new_robots))

        for idx, cost in enumerate(costs):
            if max_materials_necessary[idx] > robots[idx] and all(
                material >= prize for material, prize in zip(materials, cost)
            ):
                new_materials = tuple(
                    material + robot - prize
                    for material, robot, prize in zip(materials, robots, cost)
                )
                new_robots = tuple(
                    robot + 1 if rx == idx else robot for rx, robot in enumerate(robots)
                )
                queue.append((-new_robots[3], time_left - 1, new_materials, new_robots))

    return result, counter


def main1(time_horizon=24):
    inputs = read_input()
    result = 0
    for idx, factory in enumerate(inputs, 1):
        start_time = time.time()
        best_geodes, steps = optimize_factory_heaped(factory, time_horizon)
        print(
            f"Factory {idx} for {time_horizon} minutes optimization took {time.time() - start_time: 0.2f} s "
            f"and {steps/1_000_000:0.3f} M steps."
        )
        result += best_geodes * idx

    print(f"The result for solution 1 is: {result}")


def main2(time_horizon=32):
    inputs = read_input()
    result = 1
    for idx, factory in enumerate(inputs[:3], 1):
        start_time = time.time()
        best_geodes, steps = optimize_factory_heaped(factory, time_horizon)
        print(
            f"Factory {idx} for {time_horizon} minutes optimization took {time.time() - start_time:0.2f} s "
            f"and {steps/1_000_000:0.3f} M steps."
        )
        result *= best_geodes

    print(f"The result for solution 1 is: {result}")


if __name__ == "__main__":
    main1()
    main2()
