import intcode
import os
import pathlib
import sys
import intcode as intcode


os.system("cls")
cwd = os.getcwd()


sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent / "lib"))


def run_script(codes, script):
    computer = intcode.IntCode(codes)

    inputs = [ord(x) for x in "".join(cmd + "\n" for cmd in script)]
    output = ""

    while True:
        res = computer.run()
        if res == intcode.R_HALT:
            break

        elif res == intcode.R_INPUT:
            computer.write(inputs.pop(0))

        elif res == intcode.R_OUTPUT:
            data = computer.read()
            if data < 128:
                output += chr(data)
            else:
                output = data

    return output


def run():
    input_file = f"{cwd}/CP/AdventOfCode/_2019_Event/_21_SpringdroidAdventure.txt"

    program = open(input_file).read().strip()
    codes = [int(x) for x in program.split(",")]

    script = ["NOT C T", "NOT A J", "OR T J", "AND D J", "WALK"]
    output = run_script(codes, script)
    print(f"Walk output: {output}")

    script = [
        "OR H J",  # J=0 if H is hole
        "NOT C T",  # T=1 if C is hole
        "AND T J",  # jump if C is hole and H is not hole
        "NOT T T",  # T=0 if C is hole
        "OR F T",  # T=0 if C is hole and F is hole
        "NOT T T",  # T=1 if C is hole AND F is hole
        "OR T J",  # jump if C is hole and F is hole
        "NOT B T",  # T=1 if B is hole
        "OR T J",  # jump if B is hole
        "NOT A T",  # T=1 if A is hole
        "OR T J",  # jump if A is hole
        "AND D J",  # jump if D is not hole
        "RUN",
    ]

    output = run_script(codes, script)
    print(f"Run output: {output}")


if __name__ == "__main__":
    run()
    sys.exit(0)
