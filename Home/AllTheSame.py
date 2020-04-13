'''
All the Same

We have prepared a set of Editor's Choice Solutions. You will see them first after you solve the mission. In order to see all other solutions you should change the filter.
In this mission you should check if all elements in the given list are equal.

Input:
List.

Output:
Bool.

Example:
all_the_same([1, 1, 1]) == True
all_the_same([1, 2, 1]) == False
all_the_same(['a', 'a', 'a']) == True
all_the_same([]) == True

The idea for this mission was found on Python Tricks series by Dan Bader

Precondition:
all elements of the input list are hashable

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    return True


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''
# typing : 순환 참조 에러 방지
from typing import List, Any


def all_the_same(elements: List[Any]):
    # your code here
    # set은 중복 허용이 안됨(중복이 안되므로 값이 같다는 걸 의미)
    # elements를 set으로 만드면 중복은 삭제 되고 그 갯수를 세어 1개 이하이면 모든 값이 같는것을 의미
    return len(set(elements)) <= 1


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
