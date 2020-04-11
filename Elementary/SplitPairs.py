'''
Split Pairs

Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: 
A string.

Output: 
An iterable of strings.

Example:

split_pairs('abcd') == ['ab', 'cd']
split_pairs('abc') == ['ab', 'c_']

Precondition: 
0<=len(str)<=100

def split_pairs(a):
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''
# Case1 - itertools, operator 모듈 사용
# itertools : 반복자 생성 모듈
# operator : 파이썬의 내장 연산자에 해당하는 효율적인 함수 집합 모듈

import itertools
import operator


def split_pairs(a):
    # 리스트끼리 연결 하는 chain을 사용한다.
    connection_character = itertools.chain(a, '_')
    # 원본 리스트를 변경하지 않고 새 리스트를 생성하는 map를 사용하여 돌려준다.
    # 리스트를 이어서 반환해준다.
    return map(operator.add, connection_character, connection_character)


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")


# Case2


def split_pairs2(a):
    # a의 문자의 갯수를 변수에 할당
    len_split_pairs = len(a)
    # 문자의 갯수가 0이면
    if len_split_pairs == 0:
        # 빈 리스트 반환
        return []
    # 문자의 갯수가 1개이면
    if len_split_pairs == 1:
        # a와 _ 를 합쳐서 반환
        return [a + '_']
    # 문자의 갯수가 1개 이상이면 a를 2번째까지 슬라이싱해서 반환
    else:
        return [a[:2]] + split_pairs2(a[2:])


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs2('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs2('abcd')) == ['ab', 'cd']
    assert list(split_pairs2('abc')) == ['ab', 'c_']
    assert list(split_pairs2('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs2('a')) == ['a_']
    assert list(split_pairs2('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
