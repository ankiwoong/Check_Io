'''
First Word (simplified)

You are given a string where you have to find its first word.

This is a simplified version of the First Word mission.

Input string consists of only english letters and spaces.
There aren’t any spaces at the beginning and the end of the string.

Input:
A string.

Output:
A string.

Example:
first_word("Hello world") == "Hello"
1
How it is used: The first word is a command in a command line.

Precondition: Text can contain a-z, A-Z and spaces.

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
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")

'''


def first_word(text: str):
    # strip하고 split를 사용하여 문자를 잘라낸다.
    text = text.strip().split()
    # 리턴값은 입력받은 값에 맨 처음 단어만 출력해야되므로 인덱싱 번호는 0을 출력한다.
    return text[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")
