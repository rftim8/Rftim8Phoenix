import os.path
import re

os.system("cls")
cwd = os.getcwd()


def get_bots(values):
    r = re.compile("pos=<([0-9-]+),([0-9-]+),([0-9-]+)>, r=([0-9]+)")
    bots = []
    for cur in values:
        if cur.startswith("#"):
            print("# Note: " + cur)
        else:
            m = r.search(cur)
            if m is None:
                print(cur)
            bots.append([int(x) for x in m.groups()])
    return bots


def calc(values):
    bots = get_bots(values)
    best_i = None
    best_val = None
    for i in range(len(bots)):
        if best_i is None or bots[i][3] > best_val:
            best_val = bots[i][3]
            best_i = i

    bx, by, bz, bdist = bots[best_i]

    ret = 0

    for i in range(len(bots)):
        x, y, z, _dist = bots[i]

        if abs(x - bx) + abs(y - by) + abs(z - bz) <= bdist:
            ret += 1

    return ret


def find(done, bots, xs, ys, zs, dist, ox, oy, oz, forced_count):
    at_target = []

    for x in range(min(xs), max(xs) + 1, dist):
        for y in range(min(ys), max(ys) + 1, dist):
            for z in range(min(zs), max(zs) + 1, dist):
                count = 0
                for bx, by, bz, bdist in bots:
                    if dist == 1:
                        calc = abs(x - bx) + abs(y - by) + abs(z - bz)
                        if calc <= bdist:
                            count += 1
                    else:
                        calc = abs((ox + x) - (ox + bx))
                        calc += abs((oy + y) - (oy + by))
                        calc += abs((oz + z) - (oz + bz))
                        if calc // dist - 3 <= (bdist) // dist:
                            count += 1

                if count >= forced_count:
                    at_target.append((x, y, z, count, abs(x) + abs(y) + abs(z)))

    while len(at_target) > 0:
        best = []
        best_i = None

        for i in range(len(at_target)):
            if best_i is None or at_target[i][4] < best[4]:
                best = at_target[i]
                best_i = i

        if dist == 1:
            return best[4], best[3]
        else:
            xs = [best[0], best[0] + dist // 2]
            ys = [best[1], best[1] + dist // 2]
            zs = [best[2], best[2] + dist // 2]
            a, b = find(done, bots, xs, ys, zs, dist // 2, ox, oy, oz, forced_count)
            if a is None:
                at_target.pop(best_i)
            else:
                return a, b

    return None, None


def calc2(values):
    bots = get_bots(values)

    xs = [x[0] for x in bots] + [0]
    ys = [x[1] for x in bots] + [0]
    zs = [x[2] for x in bots] + [0]

    dist = 1
    while (
        dist < max(xs) - min(xs) or dist < max(ys) - min(ys) or dist < max(zs) - min(zs)
    ):
        dist *= 2

    ox = -min(xs)
    oy = -min(ys)
    oz = -min(zs)

    span = 1
    while span < len(bots):
        span *= 2
    forced_check = 1
    tried = {}

    best_val, best_count = None, None

    while True:
        if forced_check not in tried:
            tried[forced_check] = find(
                set(), bots, xs, ys, zs, dist, ox, oy, oz, forced_check
            )
        test_val, test_count = tried[forced_check]

        if test_val is None:
            if span > 1:
                span = span // 2
            forced_check = max(1, forced_check - span)
        else:
            if best_count is None or test_count > best_count:
                best_val, best_count = test_val, test_count
            if span == 1:
                break
            forced_check += span

    print("The max count I found was: " + str(best_count))
    return best_val


def run(values):
    print("Nearest the big bot: " + str(calc(values)))
    print("Best location value: " + str(calc2(values)))


def load_and_run(filename):
    print("------ %s ------" % (filename,))
    values = []
    with open(f"{cwd}/CP/AdventOfCode/_2018_Event/{filename}") as f:
        for cur in f:
            values.append(cur.strip("\r\n"))
    run(values)


def main():
    load_and_run("_23_ExperimentalEmergencyTeleportation.txt")


if __name__ == "__main__":
    main()
