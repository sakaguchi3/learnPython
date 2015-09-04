import random as r


def nothing():
    pass


d: dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

print("------------------- key, val")
for k, v in d.items():
    print(k, v)

print("------------------- key1")
for k in d:
    print(k)

print("------------------- key2")
for k in d.keys():
    print(k)


print("------------------- val")
for v in d.values():
    print(v)

print("-------------------")
print("-------------------")
print("-------------------")


nothing()
