from typing import Dict, List


def repeat(str: str, num: int) -> str:
    s2: List[str] = [str for i in range(0, num)]
    v: str = ', '.join(s2)
    return v


def main():
    repeatStr: str = repeat("bow", 8)
    print(repeatStr)
    pass


if __name__ == "__main__":
    main()
