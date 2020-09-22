# !/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
class exercise
"""

from typing import List


class ClassA:
    def __init__(self, l: List[str], name: str):
        self.fruits: List[str] = [f for f in l]
        self.name = name


class ClassB:

    def __init__(self, l: List[str], name: str):
        self.fruits: List[str] = [f for f in l]
        self.name = name

    def __str__(self):
        s = "ClassB[ fruits:" + ''.join(self.fruits) + " ]"
        return s


def use3():
    a1 = ClassA(name="a1", l=['banana'])
    c1 = ClassB(name="c1", l=[])
    c2 = ClassB(name="c2", l=['apple'])
    print(a1)
    print(c1)
    print(c2)
    pass


if __name__ == '__main__':
    use3()
    pass

pass
