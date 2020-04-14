'''
Acceptable Password IV

In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.

Input:
A string.

Output:
A bool.

Example:
is_acceptable_password('short') == False
is_acceptable_password('short54') == True
is_acceptable_password('muchlonger') == True
is_acceptable_password('ashort') == False
is_acceptable_password('muchlonger5') == True
is_acceptable_password('sh5') == False
is_acceptable_password('1234567') == False
is_acceptable_password('12345678910') == True

How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.


# Taken from mission Acceptable Password III

def is_acceptable_password(password: str):
    # password에 길이가 6이하이면 False
    if len(password) <= 6:
        return False
    # password가 모두 문자열이거나 숫자인경우 False
    # isalpha() : 모두 문자열인 경우 True
    # isdigit() : 모두 숫자인 경우 True
    if password.isalpha() or password.isdigit():
        return False
    # password가 문자열과 숫자로 이루어진 경우 True
    # isalnum() : 알파벳과 숫자로 이루어진 문자열인 경우 True
    if password.isalnum():
        return True
    # 그 외에 경우 False
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(password: str) -> bool:
    # your code here
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


def is_acceptable_password(password: str):
    # 조건 1 : 길이는 6보다 커야합니다.
    condition_one = len(password) > 6
    # 조건 2 : 하나 이상의 숫자를 포함해야하지만 숫자만으로는 구성 할 수 없습니다.
    condition_two = any(map(str.isdigit, password)) and not password.isdigit()
    # 조건 3 : 숫자가 있거나 숫자만 포함하는 것은 9보다 긴 암호에는 적용되지 않습니다.
    condition_three = len(password) > 9
    # 모든 조건을 비교해서 반환
    # A and B
    # A, B 둘 다 참이면 B 를 출력
    # A, B 둘 다 거짓이면 A 를 출력
    # A, B 둘 중에 하나만 참이면 거짓인 값을 출력
    # A or B
    # A, B 둘 다 참이면 A 를 출력
    # A, B 둘 다 거짓이면 B 를 출력
    # A, B 둘 중에 하나만 참이면 참인 값을 출력
    return condition_one and (condition_two or condition_three)


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
