import random as r


def nothing():
    pass


randNum: int = r.randint(0, 30)

lst1: list = [1, 2, 3]
v1: list = list(map(lambda x: x * 2, lst1))

lst2: list = [1, 2, 3]
v2: list = list(filter(lambda x: x % 2 == 1, lst2))

print(type(v1))

nothing()
