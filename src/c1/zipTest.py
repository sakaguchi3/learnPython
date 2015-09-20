'''
zip function test
'''
from builtins import int, str
from typing import Tuple, List


def makeLstTuple() -> Tuple[List[int], List[str]]:
    lst1 = [i for i in range(0, 5)]
    lst2 = ['id_' + str(100 - i) for i in range(0, 10)]
    return (lst1, lst2)


def myZip(tup: Tuple[List[int], List[str]]) -> List[str]:
    lst = [_str + '_' + str(_int) for _int, _str in zip(t[0], t[1])]
    return lst


if __name__ == '__main__':
    t = makeLstTuple()
    r = myZip(t)
    pass

