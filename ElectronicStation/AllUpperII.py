'''
All Upper II

The mission is in Reviewing Mode. You can't see the solutions Leader Board, but you can see other user solutions through the Random Review after you solve the mission.
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return False.

Input:
A string.

Output:
a boolean.

Example:
is_all_upper('ALL UPPER') == True
is_all_upper('all lower') == False
is_all_upper('mixed UPPER and lower') == False
is_all_upper('') == False

Precondition:
a-z, A-Z, 1-9 and spaces

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
    assert is_all_upper('') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


def is_all_upper(text: str):
    # true에 해당하는 조건이 모든 문자열이 대문자인지만 보면 되므로 isupper로 대문자면 True 아니면 False를 반환한다.
    return text.isupper()


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
