'''
Acceptable Password VI

In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
a string should not contain the word "password" in any case;
should contain 3 different letters (or digits) even if it is longer than 10

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
is_acceptable_password('password12345') == False
is_acceptable_password('PASSWORD12345') == False
is_acceptable_password('pass1234word') == True
is_acceptable_password('aaaaaa1') == False
is_acceptable_password('aaaaaabbbbb') == False

How it’s used:
For password verification form. Also it's good to learn how the task can be evaluated.

# Taken from mission Acceptable Password V

def is_acceptable_password(a):
    # 조건 1 : 길이는 6보다 커야합니다.
    condition_one = len(a) > 6
    # 조건 2 : 하나 이상의 숫자를 포함해야하지만 숫자만으로는 구성 할 수 없습니다.
    condition_two = any(map(str.isdigit, a)) and not a.isdigit()
    # 조건 3 : 숫자가 있거나 숫자 만 포함하는 것은 9보다 긴 암호에는 적용되지 않습니다.
    condition_three = len(a) > 9
    # 조건 4 : 문자열은 "password"라는 단어를 포함해서는 안됩니다
    condition_four = 'password' not in a.lower()
    # 모든 조건을 비교해서 반환
    # A and B
    # A, B 둘 다 참이면 B 를 출력
    # A, B 둘 다 거짓이면 A 를 출력
    # A, B 둘 중에 하나만 참이면 거짓인 값을 출력
    # A or B
    # A, B 둘 다 참이면 A 를 출력
    # A, B 둘 다 거짓이면 B 를 출력
    # A, B 둘 중에 하나만 참이면 참인 값을 출력
    return condition_one and (condition_two or condition_three) and condition_four

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
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(a):
    # your code here
    return None


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
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    assert is_acceptable_password('aaaaaa1') == False
    assert is_acceptable_password('aaaaaabbbbb') == False
    assert is_acceptable_password('aaaaaabb1') == True
    assert is_acceptable_password('abc1') == False
    assert is_acceptable_password('abbcc12') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''
# Taken from mission Acceptable Password V


def is_acceptable_password(a: str):
    # 조건 1 : 길이는 6보다 커야합니다.
    condition_one = len(a) > 6
    # 조건 2 : 하나 이상의 숫자를 포함해야하지만 숫자만으로는 구성 할 수 없습니다.
    condition_two = any(map(str.isdigit, a)) and not a.isdigit()
    # 조건 3 : 숫자가 있거나 숫자 만 포함하는 것은 9보다 긴 암호에는 적용되지 않습니다.
    condition_three = len(a) > 9
    # 조건 4 : 문자열은 "password"라는 단어를 포함해서는 안됩니다
    condition_four = 'password' not in a.lower()
    # condition_five : 3개의 다른 구성 문자
    # set는 중복을 허용하지 않는다. 그러므로 중복되지 않은 문자가 3개 이상이면 >= 3을 준다.
    condition_five = len(set(a)) >= 3
    # 모든 조건을 비교해서 반환
    # A and B
    # A, B 둘 다 참이면 B 를 출력
    # A, B 둘 다 거짓이면 A 를 출력
    # A, B 둘 중에 하나만 참이면 거짓인 값을 출력
    # A or B
    # A, B 둘 다 참이면 A 를 출력
    # A, B 둘 다 거짓이면 B 를 출력
    # A, B 둘 중에 하나만 참이면 참인 값을 출력
    return condition_one and (condition_two or condition_three) and condition_four and condition_five


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
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    assert is_acceptable_password('aaaaaa1') == False
    assert is_acceptable_password('aaaaaabbbbb') == False
    assert is_acceptable_password('aaaaaabb1') == True
    assert is_acceptable_password('abc1') == False
    assert is_acceptable_password('abbcc12') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
