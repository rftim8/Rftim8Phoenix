import os
import pathlib
import sys
from collections import deque


os.system("cls")
cwd = os.getcwd()


sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent / "lib"))


class Deck:
    def __init__(self, size):
        self.deck = deque(range(size))
        self.dir = 1

    def new(self):
        self.dir = -self.dir

    def cut(self, n):
        self.deck.rotate(-n * self.dir)

    def deal(self, incr):
        deck = deque(range(len(self.deck)))

        while len(self.deck):
            deck[0] = self.deck.popleft() if self.dir == 1 else self.deck.pop()
            deck.rotate(-incr)

        self.deck = deck
        self.dir = 1

    def cards(self):
        return list(self.deck) if self.dir == 1 else list(self.deck)[::-1]


def run():
    card = 2019
    size = 10007

    input_file = f"{cwd}/CP/AdventOfCode/_2019_Event/_22_SlamShuffle.txt"
    lines = open(input_file).read().strip()

    deck = Deck(size)
    for cmd in lines.split("\n"):
        op, *_, n = cmd.split(" ")
        if op == "cut":
            deck.cut(int(n))
        elif op == "deal" and n == "stack":
            deck.new()
        elif op == "deal":
            deck.deal(int(n))

    idx = deck.cards().index(card)
    print(f"Position of card {card}: {idx}")


run()


m = 119315717514047
n = 101741582076661
pos = 2020
shuffles = {
    "deal with increment ": lambda x, m, a, b: (a * x % m, b * x % m),
    "deal into new stack": lambda _, m, a, b: (-a % m, (m - 1 - b) % m),
    "cut ": lambda x, m, a, b: (a, (b - x) % m),
}

a, b = 1, 0
with open(f"{cwd}/CP/AdventOfCode/_2019_Event/_22_SlamShuffle.txt") as f:
    for s in f.read().strip().split("\n"):
        for name, fn in shuffles.items():
            if s.startswith(name):
                arg = int(s[len(name) :]) if name[-1] == " " else 0
                a, b = fn(arg, m, a, b)
                break
r = (b * pow(1 - a, m - 2, m)) % m

print(f"Card at #{pos}: {((pos - r) * pow(a, n*(m-2), m) + r) % m}")
