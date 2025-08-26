import os
import pathlib
import sys

os.system("cls")
cwd = os.getcwd()


sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent / "lib"))


def phase(sequence, offset=0):
    output = [0 for _ in sequence]

    if offset > len(sequence) * 0.5:
        sequence_sum = sum(sequence[offset:])
        for n in range(offset, len(sequence)):
            output[n] = sequence_sum % 10
            sequence_sum -= sequence[n]

    else:
        for i in range(offset, len(sequence)):
            step = i + 1
            mult = 1

            for n in range(step - 1, len(sequence), step * 2):
                output[i] += sum(sequence[n : n + step]) * mult
                mult *= -1

            output[i] = abs(output[i]) % 10

    return output


def run():
    input_file = (
        f"{cwd}/CP/AdventOfCode/_2019_Event/_16_FlawedFrequencyTransmission.txt"
    )
    line = open(input_file).read().strip()

    sequence = [int(x) for x in line]

    msg = sequence.copy()
    for _ in range(100):
        msg = phase(msg)

    output = "".join(str(n) for n in msg[:8])
    print(f"First eight of final output: {output}")

    offset = int("".join(str(n) for n in sequence[:7]))
    msg = sequence * 10000
    for n in range(100):
        msg = phase(msg, offset)

    output = "".join(str(n) for n in msg[offset : offset + 8])
    print(f"Embedded message: {output}")


if __name__ == "__main__":
    run()
    sys.exit(0)
