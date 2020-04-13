'''
Digits Multiplication

We have prepared a set of Editor's Choice Solutions. You will see them first after you solve the mission. In order to see all other solutions you should change the filter.
juggler
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example:
 The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input:
A positive integer.

Output:
The product of the digits as an integer.

Example:
checkio(123405) == 120
checkio(999) == 729
checkio(1000) == 1
checkio(1111) == 1

How it is used: 
This task can teach you how to solve a problem with simple data type conversion.

Precondition: 
0 < number < 106

def checkio(number: int) -> int:
    
    return 1


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
'''


def checkio(number: int):
    # 초기값
    initial_value = 1

    #  조건 판단 (0은 False 이외 True)
    for i in str(number):
        if int(i):
            # 0이 아니면 initial_value에 누적
            initial_value *= int(i)

    return initial_value


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
