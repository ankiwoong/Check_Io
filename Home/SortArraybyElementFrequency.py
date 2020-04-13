'''
Sort Array by Element Frequency

Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input:
Iterable

Output:
Iterable

Example:
frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']

Precondition: 
elements can be ints or strings

The mission was taken from Python CCPS 109 Fall 2018. It's being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen


def frequency_sort(items):
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


def frequency_sort(items):
    """Given a list, sorts the list based on item frequency.
        Ties are solved by first to appear in the list."""

    # 고유 한 키를 찾아 표시된 순서대로 목록에 저장하십시오.
    keys = []
    for item in items:
        if not item in keys:
            keys.append(item)

    # KEY와 FREQ를 튜플 목록으로 변경
    (KEY, FREQ) = (0, 1)
    freq_dict = []  # [(KEY, FREQ), ...]
    for key in keys:
        freq_dict.append((key, items.count(key)))

    # 딕셔너리를 사용해서 정렬된 목록을 구성
    sorted_list = []
    while freq_dict:
        highest_freq_pair = ("", 0)
        for entry in freq_dict:
            if entry[FREQ] > highest_freq_pair[FREQ]:
                highest_freq_pair = (entry[KEY], entry[FREQ])

        sorted_list += [highest_freq_pair[KEY]] * highest_freq_pair[FREQ]
        freq_dict.remove(highest_freq_pair)
        # freq_dict가 비어 있으면 루프가 종료됩니다.

    return sorted_list


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [
        4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == [
        'bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
