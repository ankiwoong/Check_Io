'''
End Zeros

Try to find out how many zeros a given number has at the end.

Input:
A positive Int

Output:
An Int.

Example:
end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0

def end_zeros(num: int) -> int:
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''

# Case 1 - rstip 사용


def end_zeros(num: int):
    # num을 문자로 변환후 우측에서부터 0을 제거해서 다른 숫자가 나올때까지 한 후 그 길이를 빼면 숫자가 나온다.
    return len(str(num)) - len(str(num).rstrip('0'))


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")


# Case 2 - for 사용


def end_zeros_2(num):
    # 초기값을 변수 n에 0을 지정
    n = 0
    # num을 문자로 변경하고 배열을 거꾸로 뒤집는다.
    for i in reversed(str(num)):
        # i가 0이면 변수 n에 값을 1씩 증가
        if i == '0':
            n += 1
        # i가 0이 아니면 변수 n을 돌려주면서 for문 종료
        else:
            return n
    # 최종적으로 n을 리턴한다.
    return n


if __name__ == '__main__':
    print("Example:")
    print(end_zeros_2(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros_2(0) == 1
    assert end_zeros_2(1) == 0
    assert end_zeros_2(10) == 1
    assert end_zeros_2(101) == 0
    assert end_zeros_2(245) == 0
    assert end_zeros_2(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
