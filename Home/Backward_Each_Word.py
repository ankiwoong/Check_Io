'''
Backward Each Word

In a given string you should reverse every word, but the words should stay in their places.

Input:
A string.

Output:
A string.

Example:
backward_string_by_word('') == ''
backward_string_by_word('world') == 'dlrow'
backward_string_by_word('hello world') == 'olleh dlrow'
backward_string_by_word('hello   world') == 'olleh   dlrow'

Precondition:
The line consists only from alphabetical symbols and spaces.

def backward_string_by_word(text: str) -> str:
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


def backward_string_by_word(text: str):
    # text를 공백으로 나눠서 하나씩 가져와서
    for i in text.split():
        # text를 i와 스텝을 뒤에서 하나씩 가져온다.
        text = text.replace(i, i[::-1])
    # text를 반환한다
    return text


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
