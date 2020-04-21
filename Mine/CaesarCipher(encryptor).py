'''
Caesar Cipher (encryptor)

This mission is the part of the set. Another one - Caesar cipher decriptor.

Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.) using Caesar cipher where each letter of input text is replaced by another that stands at a fixed distance. For example ("a b c", 3) == "d e f"

example

Input:
A secret message as a string (lowercase letters only and white spaces)

Output:
The same string, but encrypted

Example:
to_encrypt("a b c", 3) == "d e f"
to_encrypt("a b c", -3) == "x y z"
to_encrypt("simple text", 16) == "iycfbu junj"
to_encrypt("important text", 10) == "swzybdkxd dohd"
to_encrypt("state secret", -13) == "fgngr frperg"

How it is used:
For cryptography and to save important information.

Precondition:
0 < len(text) < 50
-26 < delta < 26


def to_encrypt(text, delta):
    #replace this for solution
    return text

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''
import string


def to_encrypt(text, delta):
    # string.ascii_lowercase : 소문자 'abcdefghijklmnopqrstuvwxyz'
    # ex> text = 'abc' / delta = 10
    # 'klmnopqrstuvwxyzabcdefghij'
    alpha_after = string.ascii_lowercase[delta:] + \
        string.ascii_lowercase[:delta]
    # translate : 문자열 안의 문자를 다른 문자로 변경
    # translate(str.maketrans('바꿀문자', '새문자'))을 사용하면 문자를 바꾼 뒤 결과를 반환한다
    # ex> klm
    # https://dojang.io/mod/page/view.php?id=2299
    table = str.maketrans(string.ascii_lowercase, alpha_after)
    return text.translate(table)


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
