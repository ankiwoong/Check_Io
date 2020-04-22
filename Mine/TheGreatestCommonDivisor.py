'''
The Greatest Common Divisor

"[The Euclidean algorithm] is the granddaddy of all algorithms, because it is the oldest nontrivial algorithm that has survived to the present day."
-- Donald Knuth, The Art of Computer Programming, Vol. 2: Seminumerical Algorithms, 2nd edition (1981).

The greatest common divisor (GCD), also known as the greatest common factor of two or more integers (at least one of which is not zero), is the largest positive integer that divides a number without a remainder. For example, the GCD of 8 and 12 is 4.

You are given an arbitrary number of positive integers. You should find the greatest common divisor for these numbers.

Input:
An arbitrary number of positive integers.

Output:
The greatest common divisor as an integer.

Example:
great_common_divisor(6, 4) == 2
great_common_divisor(2, 4, 8) == 2

How it is used:
GCD is a basic concept found in mathematically oriented software. This is a good example of a simple algorithm which has many possible applications.

Precondition:
1 < len(args) ≤ 10
all(0 < x ≤ 2 ** 32 for x in args)

def greatest_common_divisor(*args):
    """
        Find the greatest common divisor
    """
    return 1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
'''


from functools import reduce
from math import gcd

# 최대공약수(GCD(greatest common divisor)) : 주어진 두 수 x, y에서 x의 약수이면서 y의 약수인 수 중 최대값


def greatest_common_divisor(*args):
    # reduce(함수, 계산하고자 하는 리스트)
    # 단일 값으로 반환
    # reduce를 사용하면 최대값을 구할 수 있다.
    return reduce(gcd, args)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
