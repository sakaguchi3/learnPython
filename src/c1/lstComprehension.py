# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from builtins import int
from typing import List, Tuple


def tuple_f():
    lst1: List[int] = [i for i in range(0, 10)]
    lst2: List[int] = [i for i in range(0, 20) if i % 2 == 1]

    lst3: List[Tuple[int, int]] = [(i, 100 - j) for i in range(0, 2) for j in range(0, 3)]
    return None
    pass


def zipWithIndex():
    lst: List[str] = ['Alice', 'Bob', 'Charlie']
    enum_lst: List[Tuple[int, str]] = [(i, name) for i, name in enumerate(lst)]
    pass

if __name__ == '__main__':
    print('start')
    pass

pass
