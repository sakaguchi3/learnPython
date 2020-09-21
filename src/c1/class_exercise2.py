# !/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
class exercise
"""

from typing import List


class ClassA():
    '''static field'''
    fruits = []

    def __init__(self, l: List[str]):
        for f in l:
            self.fruits.append(f)
        pass

    def show(self):
        print("fruts:{}".format(self.fruits))


def use2():
    print("empty -------------")
    c1 = ClassA([])
    c1.show()

    print("apple -------------")
    c2 = ClassA(['apple'])
    c2.show()
    c1.show()
    pass


if __name__ == '__main__':
    use2()
    pass
pass
