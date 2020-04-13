'''
Acceptable Password III

In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but cannot consist of just digits.

Input:
A string.

Output:
A bool.

Example:
is_acceptable_password('short') == False
is_acceptable_password('muchlonger') == False
is_acceptable_password('ashort') == False
is_acceptable_password('muchlonger5') == True
is_acceptable_password('sh5') == False
is_acceptable_password('1234567') == False

How it’s used:
For password verification form. Also it's good to learn how the task can be evaluated.


# Taken from mission Acceptable Password II

def is_acceptable_password(password: str):
    # 길이가 6이상이고 숫자를 포함하고 있으면 참
    if len(password) > 6 and any(map(str.isdigit, password)):
        return True
    # 그 외에는 거짓
    else:
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
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(password: str) -> bool:
    # your code here
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
'''


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
