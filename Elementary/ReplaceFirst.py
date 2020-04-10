'''
Replace First

In a given list the first element should become the last one. An empty list or list with only one element should stay the same.

example

Input: 
List.

Output: 
Iterable.

Example:
replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
replace_first([1]) == [1]

from typing import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    return items


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''
from typing import Iterable


def replace_first(items: list) -> Iterable:
    # items 리스트의 길이가 0 이상이면
    if len(items) > 0:
        # 첫 번째 원소를 가져올 리스트 생성
        first_list = []
        # 첫 번째 원소를 for 문을 사용하여 가져옴
        for i in items[:1]:
            first_list.append(i)
        # 리스트의 2번째 원소부터 가져와서 맨 앞 원소가 뒤로 가야되므로 더하기로 구성
        return items[1:] + first_list
    # 빈리스트일 경우 items를 그대로 반환
    else:
        return items


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
