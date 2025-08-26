import os

os.system("cls")


def rft_dictionary():
    a = {"a": 2, "b": 3, "c": 4, "d": 5}
    b = a.get("b")
    c = a.keys()
    d = a.items()

    a["b"] = 15
    a.update({"c": 10})
    a.pop("d")

    print(f"Item at key 'b':  {b}")
    print(f"Keys: {c}")
    print(f"Items: {d}")


def add_item_if_not_exists_else_increment():
    a = {}
    a["test"] = a.get("test", 0) + 1
    print(a)


add_item_if_not_exists_else_increment()
# rft_dictionary()
