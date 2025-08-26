import os
import pathlib
import sys
import intcode as intcode


os.system("cls")
cwd = os.getcwd()


sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent / "lib"))


def run_network(codes, address=None):
    computers = {}
    q = {}

    initialized = set()
    active = set()
    idle = set()

    nat = (None, None)
    nat_sent_y = None

    for i in range(50):
        computers[i] = intcode.IntCode(codes)
        q[i] = []
        active.add(i)

    run = True
    x, y = None, None

    while run:
        all_idle = True

        for i, c in computers.items():
            if i not in active:
                continue

            res = c.run()

            if res == intcode.R_HALT:
                active -= {i}
                break

            elif res == intcode.R_INPUT:
                if i not in initialized:
                    initialized.add(i)
                    c.write(i)

                    idle.discard(i)
                    all_idle = False

                elif len(q[i]):
                    x, y = q[i].pop(0)
                    c.write(x)
                    c.write(y)

                    idle.discard(i)
                    all_idle = False

                else:
                    c.write(-1)
                    if i not in idle:
                        idle.add(i)
                        all_idle = False

            elif res == intcode.R_OUTPUT:
                idle.discard(i)
                all_idle = False

                dest = c.read()
                _ = c.run()
                x = c.read()
                _ = c.run()
                y = c.read()

                if dest in q:
                    q[dest].append((x, y))

                else:
                    if address is not None and address == dest:
                        run = False
                        break

                    if dest == 255:
                        nat = (x, y)

            elif res == intcode.R_INVALID:
                print(
                    f"Computer {i} error @ {c.ptr}: {','.join(str(x) for x in c.code)}"
                )
                run = False
                break

        if all_idle:
            nx, ny = nat

            if nat_sent_y is not None and nat_sent_y == ny:
                x, y = nx, ny
                run = False

            else:
                nat_sent_y = ny
                q[0].append((nx, ny))

    return (x, y)


def run():
    input_file = f"{cwd}/CP/AdventOfCode/_2019_Event/_23_CategorySix.txt"

    program = open(input_file).read().strip()
    codes = [int(x) for x in program.split(",")]

    x, y = run_network(codes, 255)
    print(f"Packet at address 255: {(x, y)}")

    _, y = run_network(codes)
    print(f"First resent NAT Y address {y}")


if __name__ == "__main__":
    run()
    sys.exit(0)
