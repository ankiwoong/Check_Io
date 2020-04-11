'''
Split List

You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should have more elements. If it has no elements, then two empty arrays should be returned.

example

Input:
Array.

Output:
Array or two arrays.

Example:
split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
split_list([1, 2, 3]) == [[1, 2], [3]]

def split_list(items: list) -> list:
    # your code here
    return [items]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


def split_list(items: list):
    # 나눌 인덱스 번호를 구하기 위해서 items에 원소갯수를 2로 나눈 나머지에 2를 더하고 다시 원소갯수로 나눈 몫을 가져온다.
    item_index_number = len(items) // 2 + len(items) % 2
    # 그렇게 구한 인덱스 번호를 슬라이싱을 통해서 가져와서 반환한다.
    return [items[:item_index_number], items[item_index_number:]]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
