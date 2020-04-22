'''
Can Balance

Each item in the list of items is considered to be a physical weight, and guaranteed to be a positive integer. Your task is to find and return a fulcrum position in this list so that when balanced on that position, the total torque of the items to the left of that position equals the total torque of the items to the right of that position. (The item on the fulcrum is assumed to be centered symmetrically on both sides, and therefore doesn’t participate in the torque calculation.)

As taught in any introductory physics textbook, the torque of an item with respect to the fulcrum equals its weight times its distance from the fulcrum. If a fulcrum position exists, return that position, otherwise return -1 to indicate that the given items cannot be balanced, at least not without being rearranged.

Input: 
The iterable of positive integers.

Output: 
Int.

Example:
# 6*2 + 1*1 == 5*1 + 4*2
can_balance([6, 1, 10, 5, 4]) == 2
# 10*1 == 3*1 + 2*2 + 1*3
can_balance([10, 3, 3, 2, 1]) == 1

The mission was taken from Python CCPS 109 Fall 2018. It’s being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen


from typing import Iterable

def can_balance(weights: Iterable) -> int:
    # your code here
    return -1


if __name__ == '__main__':
    print("Example:")
    print(can_balance([6, 1, 10, 5, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert can_balance([6, 1, 10, 5, 4]) == 2
    assert can_balance([10, 3, 3, 2, 1]) == 1
    assert can_balance([7, 3, 4, 2, 9, 7, 4]) == -1
    assert can_balance([42]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''
from typing import Iterable

# Case 1


def can_balance(weights: Iterable):
    # 무게 목록에서 받침점 색인을 찾아야 된다.
    # 가중치 리스트의 길이가 2보다 작은 경우, 받침점 인덱스는 리스트의 시작으로 간주.
    weights_len = len(weights)
    if weights_len < 2:
        return 0

    # 목록에서 위치 1부터 마지막 ​​위치까지의 가능한 각 지점에 대해 목록의 왼쪽을 더한 다음 오른쪽의 합계와 비교하십시오.
    for fulcrum_idx in range(1, weights_len-2):
        left_sum = 0
        for idx, num in enumerate(weights[0:fulcrum_idx]):
            left_sum += num * (fulcrum_idx - idx)

        right_sum = 0
        for idx, num in enumerate(weights[fulcrum_idx+1:]):
            right_sum += num * (idx + 1)

        if left_sum == right_sum:
            return fulcrum_idx

    return -1


if __name__ == '__main__':
    print("Example:")
    print(can_balance([6, 1, 10, 5, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert can_balance([6, 1, 10, 5, 4]) == 2
    assert can_balance([10, 3, 3, 2, 1]) == 1
    assert can_balance([7, 3, 4, 2, 9, 7, 4]) == -1
    assert can_balance([42]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")

# Case 2


def can_balance2(weights: Iterable):
    # Iterable을 반복해서 사용하면 소모 될 수 있습니다. 재사용 할 튜플을 만듭니다.
    weights = tuple(weights)

    # 여기서 f는 받침점 위치이고, i는 가중치의 위치 지수입니다.
    # v는 해당 가중치의 가중치 값이므로 sum ((f-i) * v) == 0이 필요합니다.
    # 즉, f * sum (v) == sum (i * v)

    torques = sum(i*v for i, v in enumerate(weights))
    f, remainder = divmod(torques, sum(weights))
    if remainder == 0:
        return f
    return -1


if __name__ == '__main__':
    print("Example:")
    print(can_balance2([6, 1, 10, 5, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert can_balance2([6, 1, 10, 5, 4]) == 2
    assert can_balance2([10, 3, 3, 2, 1]) == 1
    assert can_balance2([7, 3, 4, 2, 9, 7, 4]) == -1
    assert can_balance2([42]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
