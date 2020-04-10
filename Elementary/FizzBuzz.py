'''
Fizz Buzz

"Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.

You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.

Input:
A number as an integer.

Output:
The answer as a string.

Example:
checkio(15) == "Fizz Buzz"
checkio(6) == "Fizz"
checkio(5) == "Buzz"
checkio(7) == "7"
    
1
2
3
4
5
6
How it is used: Here you can learn how to write the simplest function and work with if-else statements.

Precondition: 0 < number ≤ 1000

# Your optional code here
# You can import some modules or create additional functions
def checkio(number: int) -> str:
    # Your code here
    # It's main function. Don't remove this function
    # It's using for auto-testing and must return a result for check.

    # replace this for solution
    return 'Fizz Buzz'

# Some hints:
# Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio(15))
    
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
'''


def checkio(number: int):
    # 입력값을 15로 나누었을때 0이면 Fizz Buzz
    if number % 15 == 0:
        return 'Fizz Buzz'
    # 입력값을 5로 나누었을때 0이면 Buzz
    elif number % 5 == 0:
        return 'Buzz'
    # 입력값을 3로 나누었을때 0이면 Fizz
    elif number % 3 == 0:
        return 'Fizz'
    # 입력값을 str(n)으로 변환
    return str(number)


if __name__ == '__main__':
    print('Example:')
    print(checkio(15))

    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")