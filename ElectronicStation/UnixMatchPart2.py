'''
Unix Match. Part 2

Sometimes you find yourself in a situation where among a huge number of files on your computer or in a separate folder you need to find files of a certain type - for example, images with the extension '.jpg' or documents with the extension '.txt', or even files that have the word 'butterfly' in their name. Doing this manually can be time-consuming. 'Matching' or patterns for searching files by a specific mask are just what you need for these sort of challenges.
This mission will help you understand how this works.

You need to find out if the given unix pattern matches the given filename.

Here is a small table that shows symbols that can be used in patterns.

[seq]	matches any character in seq, for example [123] means any character - '1', '2' or '3'
[!seq]	matches any character not in seq, for example [!123] means any character except '1', '2' and '3'
Note that the expression in one pair of square brackets responds only for 1 character. So ('0123', '[!abc]123') == True, but ('00123', '[!abc]123') = False

Input:
Two arguments. Both are strings.

Output:
Bool.

Example:
unix_match('somefile.txt', 'somefile.txt') == True
unix_match('1name.txt', '[!abc]name.txt') == True
unix_match('log1.txt', 'log[1234567890].txt') == True

How it is used:
in the unix-shell

Precondition:
0 < len(strings) < 100

def unix_match(filename: str, pattern: str) -> bool:
    
    # your code here
    return filename == pattern


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''
import re


def unix_match(filename: str, pattern: str):
    # 일반적인 문자열은 replace를 사용하여 치환을 한다.
    # * -> \*
    # . -> \.
    # [! -> [^
    # [] -> [^.]
    # [^] -> \[!\]
    pat = pattern.replace('*', '\\*').replace('.', '\\.').replace(
        '[!', '[^').replace('[]', '[^.]').replace('[^]', '\\[!\\]')
    # 위에 만든 패턴을 filename과 매칭 해봐서 매칭이 되면 None을 돌려주므로 비교를 해서 None이면 True를 반환해준다.
    return re.match(pat, filename) is not None
    # return re.match(pat, filename) != None


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
