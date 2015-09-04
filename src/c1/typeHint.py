from typing import Dict


def nothing():
    pass


def add(x: int, y: int) -> float:
    v: int = x + y
    return float(v)


d: Dict[str, int] = {
    "a": 1,
    "b": 2,
    "c": 3
}

print("d type is {}".format(type(d)))  # dict
print("d.item type is {}".format(type(d.items())))  # dict_items
print("d.keys type is {}".format(type(d.keys())))  # dict_keys
print("d.values type is {}".format(type(d.values())))  # dict_values

ans: float = add(y=3, x=2)

# エラーにはならない
numInt: str = 3

nothing()
