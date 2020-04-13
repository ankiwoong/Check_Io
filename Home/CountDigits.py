'''
Count Digits

You need to count the number of digits in a given string.

Input: A Str.

Output: An Int.

Example:
count_digits('hi') == 0
count_digits('who is 1st here') == 1
count_digits('my numbers is 2') == 1
count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 8
count_digits('5 plus 6 is') == 2
count_digits('') == 0

def count_digits(text: str) -> int:
    # your code here
    return 0


if __name__ == '__main__':
    print("Example:")
    print(count_digits('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_digits('hi') == 0
    assert count_digits('who is 1st here') == 1
    assert count_digits('my numbers is 2') == 1
    assert count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 8
    assert count_digits('5 plus 6 is') == 2
    assert count_digits('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''

# Case 1 - 정규식

import re


def count_digits(text: str):
    # 정규화를 사용하여서 검색 문자열에서 패턴과 매칭되는 모든 경우를 찾아 리스트로 반환
    number = re.findall('[0-9]', text)
    # number의 길이를 반환해준다.
    return len(number)


if __name__ == '__main__':
    print("Example:")
    print(count_digits('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_digits('hi') == 0
    assert count_digits('who is 1st here') == 1
    assert count_digits('my numbers is 2') == 1
    assert count_digits('This picture is an oil on canvas '
                        'painting by Danish artist Anna '
                        'Petersen between 1845 and 1910 year') == 8
    assert count_digits('5 plus 6 is') == 2
    assert count_digits('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")

# Case 2


def count_digits2(text: str):
    # 초기값 설정
    result = 0

    # text를 하나씩 가져와서
    for i in text:
        # i가 숫자로 되어있다면 isdigit를 사용하여 True를 반환하게 하여 True이면
        if i.isdigit() == True:
            # result에 1씩 더한다.
            result += 1
    # result를 반환
    return result


if __name__ == '__main__':
    print("Example:")
    print(count_digits2('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_digits2('hi') == 0
    assert count_digits2('who is 1st here') == 1
    assert count_digits2('my numbers is 2') == 1
    assert count_digits2('This picture is an oil on canvas '
                         'painting by Danish artist Anna '
                         'Petersen between 1845 and 1910 year') == 8
    assert count_digits2('5 plus 6 is') == 2
    assert count_digits2('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
