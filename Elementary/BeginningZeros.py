'''
Beginning Zeros

You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

Input:
A string, that consist of digits.

Output:
An Int.

Example:
beginning_zeros('100') == 0
beginning_zeros('001') == 2
beginning_zeros('100100') == 0
beginning_zeros('001001') == 2
beginning_zeros('012345679') == 1
beginning_zeros('0000') == 4

Precondition: 
0-9

def beginning_zeros(number: str) -> int:
    # your code here
    return 0


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


def beginning_zeros(number: str):
    # 초기값 지정
    initial_value = 0
    # 숫자를 하나씩 가져와서
    for n in number:
        # n이 0이랑 같으면
        if int(n) == 0:
            # 초기값에 1을 더한다.
            initial_value += 1
        # 다른 숫자이면
        else:
            # 초기값을 반환
            return initial_value
    # for문이 종료되면 초기값에 더해진 값을 반환
    return initial_value


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")
