'''
Say Hi

We have prepared a set of Editor's Choice Solutions. You will see them first after you solve the mission. In order to see all other solutions you should change the filter.
In this mission you should write a function that introduces a person with the given parameter's attributes.

Input:
Two arguments. String and positive integer.

Output:
String.

Example:
say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"

# 1. on CheckiO your solution should be a function
# 2. the function should return the right answer, not print it.

def say_hi(name: str, age: int) -> str:
    """
        Hi!
    """
    # your code here
    return "Hi. My name is Alex and I'm 32 years old"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')
'''

# case 1 - format 함수 사용


def say_hi(name: str, age: int):
    return "Hi. My name is {} and I'm {} years old".format(name, age)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi(
        "Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi(
        "Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')


# case 2 - 리터널 구문 사용


def say_hi_2(name: str, age: int):
    return f'Hi. My name is {name} and I\'m {age} years old'


print(say_hi_2('alex', 32))
