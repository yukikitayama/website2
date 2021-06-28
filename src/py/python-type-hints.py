# If you use types other than built-in types, such as list, 
# you need to import from typing standard module
from typing import List


# Integer type hint
def func1(n: int) -> int:
    return n * n


def func2(nums: List[int]) -> int:
    return max(nums)


# Type hint with default value to argument
def func3(num: int = 0) -> int:
    return num


# If the type hint refers to a class before defined,
# type class name inside quotations as a string literal,
# otherwise, it will throw an error.
class Node:
    def insert(self, node: 'Node') -> bool:
        return True


def main():

    print(func1(2))
    # 4

    # Even if you use something other than int and as long as
    # Python can run, it returns and does not throw an error
    print(func1(2.1))
    # 4.41

    print(func2([1, 2, 3]))
    # 3

    print(func3())
    # 0


if __name__ == "__main__":
    main()
