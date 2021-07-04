# If you need list of types
from typing import List
# If multiple types are possible
from typing import Union


# Integer type hint
def func1(n: int) -> int:
    return n * n


# List of type
def func2(nums: List[int]) -> int:
    return max(nums)


# Built-in list
def func3(param: list) -> list:
    result = param.append('d')
    print(result)
    return result


# Type hint with default value to argument
def func4(num: int = 0) -> int:
    return num


# None if a function returns nothing
# Union if multiple types could be used
def func5(param: Union[int, str]) -> None:
    result = param * 2
    print(f'func4 result: {result}')


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

    param_list = ['a', 'b', 'c']
    print(func3(param_list))

    print(func4())
    # 0

    print(func5(1))

    print(func5('test'))


if __name__ == "__main__":
    main()
