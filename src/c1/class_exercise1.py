# !/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
class exercise
"""


class ClassParent():
    def func_parent(self):
        print("I am parent.")


class ClassChild(ClassParent):
    def func_child(self):
        print("I am child.")

    ''' override '''

    def func_parent(self):
        print("I am not parent.")


def use1():
    # parent
    p = ClassParent()
    p.func_parent()
    print('separate -------------')

    # child
    c = ClassChild()
    c.func_parent()
    c.func_child()

    pass


if __name__ == '__main__':
    use1()
    pass
pass
