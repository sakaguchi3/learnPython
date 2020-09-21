# !/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
class exercise
"""

from typing import List


class ClassB():

    def __init__(self, l: List[str], name: str):
        self.fruits: List[str] = [f for f in l]
        self.name = name

    def show(self):
        print("[{}] {}".format(self.name, self.fruits))


def use3():
    print("empty -------------")
    c1 = ClassB(name="c1", l=[])
    c1.show()

    print("apple -------------")
    c2 = ClassB(name="c2", l=['apple'])
    c2.show()
    c1.show()
    pass


if __name__ == '__main__':
    use3()
    pass
pass
