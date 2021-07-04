from typing import Union
import pandas as pd


def func1(param: Union[int, str]) -> None:
    param = param * 2
    print(f'In function: {param}')


def func2(param_list: list) -> None:
    param_list.append(100)
    print(f'In function: {param_list}')


def func3(df: pd.DataFrame):
    df = df.append({'col_1': 3, 'col_2': 'test'}, ignore_index=True)
    print(f'In function:\n{df}')
    return df


def main():

    # Call by value
    param1 = 1
    print(f'Before function: {param1}')
    func1(param1)
    print(f'After function: {param1}')
    print()

    param2 = 'test'
    print(f'Before function: {param2}')
    func1(param2)
    print(f'After function: {param2}')
    print()

    # Call by reference
    param_list = [0, 1, 2]
    print(f'Before function: {param_list}')
    func2(param_list)
    print(f'After function: {param_list}')
    print()
   
    # Pandas DataFrame
    df = pd.DataFrame(data={'col_1': [1, 2], 'col_2': ['Yuki', 'Kitayama']})
    print(f'Before function:\n{df}')
    df1 = func3(df)
    print(f'After function:\n{df}')
    print(f'After function:\n{df1}')
    print()

if __name__ == '__main__':
    main()
