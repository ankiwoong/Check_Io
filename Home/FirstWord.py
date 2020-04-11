'''
First Word

You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, a dot or space.
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.

Input:
A string.

Output:
A string.

Example:
first_word("Hello world") == "Hello"
first_word("greetings, friends") == "greetings"

How it is used:
the first word is a command in a command line

Precondition:
the text can contain a-z A-Z , . '

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    return text[0:2]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


def first_word(text: str):
    # replace와 strip에 위치를 주의하자.
    # replace : 문자열 변경 메소드(. -> 공백 / , -> 공백)
    # strip : 문자열 제거 메소드(공백 삭제)
    text = text.replace('.', ' ').replace(',', ' ').strip()
    # split : 문자열 나누기
    text = text.split()
    # text에 맨 앞만 리턴하면 되므로 인덱스 번호 0을 준다.
    return text[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
