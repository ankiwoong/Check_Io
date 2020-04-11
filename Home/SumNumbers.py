'''
Sum Numbers

In a given text you need to sum the numbers. Only separated numbers should be counted. If a number is part of a word it shouldn't be counted.

The text consists from numbers, spaces and english letters

Input:
A string.

Output:
An int.

Example:
sum_numbers('hi') == 0
sum_numbers('who is 1st here') == 0
sum_numbers('my numbers is 2') == 2
sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
sum_numbers('5 plus 6 is') == 11
sum_numbers('') == 0

def sum_numbers(text: str) -> int:
    # your code here
    return 0


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


def sum_numbers(text: str):
    # 입력값을 단어로 나누고
    text_list = text.split()
    # 반환할 값을 초기 설정 하고(숫자의 합)
    result = 0
    # 각 단어마다
    for word in text_list:
        # 정수로 바꿔서 정수로 바꿔지면
        try:
            # 정수를 i 변수에 할당하고
            i = int(word)
            # 그 값을 반환할 값에 더한다.
            result += i
        # 그 외에 글자랑 숫자랑 같이 있는 경우에는 다음 것을 확인 한다.
        except:
            pass
    # for문이 종료 되면 result를 반환한다.
    return result


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
