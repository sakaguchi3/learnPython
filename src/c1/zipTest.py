# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from builtins import int, str
from typing import Tuple, List


def makeLstTuple() -> Tuple[List[int], List[str]]:
    lst1 = [i for i in range(0, 5)]
    lst2 = ['id_' + str(100 - i) for i in range(0, 10)]
    return lst1, lst2


def ziptest(tup: Tuple[List[int], List[str]]) -> List[str]:
    lst: List[str] = [_str + '_' + str(_int) for _int, _str in zip(t[0], t[1])]
    return lst


if __name__ == '__main__':
    t = makeLstTuple()
    r = ziptest(t)
    pass

pass
