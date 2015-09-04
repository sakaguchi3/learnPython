from builtins import int
from typing import Dict, List


def nothing():
    pass


lst1: List[int] = [i for i in range(0, 10)]
lst2: List[int] = [i for i in range(0, 20) if i % 2 == 1]

nothing()
