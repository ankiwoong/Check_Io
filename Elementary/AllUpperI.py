'''
All Upper I

Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.

Input:
A string.

Output:
a boolean.

Example:
is_all_upper('ALL UPPER') == True
is_all_upper('all lower') == False
is_all_upper('mixed UPPER and lower') == False
is_all_upper('') == True
1
2
3
4
Precondition: a-z, A-Z, 1-9 and spaces

def is_all_upper(text: str) -> bool:
    # your code here
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


def is_all_upper(text: str):
    # 입력값이 모두 대문자면 True
    # isupper() : 입력받은 값이 모두 대문자인지 확인 / 모두 대문자이면 True
    if text.isupper() == True:
        return True
    # 입력값이 공백이면 True(strip로 스페이스가 입력되더라도 다 제거하여 공백 여부 확인)
    elif bool(text.strip()) == False:
        return True
    # 입력값이 숫자이면 True
    # isdigit() : 입력받은 것이 모두 숫자인지 확인 / 모두 숫자이면 True
    elif text.isdigit() == True:
        return True
    # 나머지는 False
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
