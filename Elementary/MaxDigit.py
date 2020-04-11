'''
Max Digit

You have a number and you need to determine which digit in this number is the biggest.

Input: 
A positive int.

Output:
An Int (0-9).

Example:
max_digit(0) == 0
max_digit(52) == 5
max_digit(634) == 6
max_digit(1) == 1
max_digit(10000) == 1

def max_digit(number: int) -> int:
    # your code here
    return 0


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


def max_digit(number: int):
    # 0이 아닌 숫자가 입력됬을때
    try:
        # 정수를 문자열로 바꾸고 그것을 리스트화 시킨다.
        number_list = list(map(int, list(str(number))))
        # 만든 리스트를 내림차순 정렬을 하면 가장 큰 숫자가 앞으로 온다.
        number_list.sort(reverse=True)
        # 초기값을 설정 해준다.
        initial_value = 0
        # 리스트에서 맨 앞이 가장 큰수이므로 가장 큰수만 초기값에 더한다.
        for i in number_list[:1]:
            initial_value += i
        # 구한 값을 반환으로 준다.
        return initial_value

    # 0이 입력 됫을경우 return을 주면 None이 출력되므로 예외처리해서 0을 돌려준다.
    except ZeroDivisionError:
        return number


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))
