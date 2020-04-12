'''
Days Between

We have prepared a set of Editor's Choice Solutions. You will see them first after you solve the mission. In order to see all other solutions you should change the filter.
How old are you in a number of days? It's easy to calculate - just subtract your birthday from today. We could make this a real challenge though and count the difference between any dates.

You are given two dates as an array with three numbers - a year, month and day. For example: 19 April 1982 will be (1982, 4, 19). You should find the difference in days between the given dates. For example between today and tomorrow = 1 day. The difference will always be either a positive number or zero, so don't forget about the absolute value.

Input:
Two dates as tuples of integers.

Output:
The difference between the dates in days as an integer.

Example:
days_diff((1982, 4, 19), (1982, 4, 22)) == 3
days_diff((2014, 1, 1), (2014, 8, 27)) == 238

How it is used: Python has batteries included, so in this mission you’ll need to learn how to use completed modules so that you don't have to invent the bicycle all over again.

Precondition:
Dates between 1 january 1 and 31 december 9999. Dates are correct.

def days_diff(a, b):
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


from datetime import datetime


def days_diff(date1, date2):
    # datetime를 사용하여서 년 월 일을 지정한다.
    # 각 년 / 월 / 일은 입력되는 인덱싱 번호로 추출한다.
    # 출력값은 year-month-day 00:00:00 로 나온다.
    date1 = datetime(year=date1[0], month=date1[1], day=date1[2])
    date2 = datetime(year=date2[0], month=date2[1], day=date2[2])
    # date2에서 date1의 날짜를 빼면 되므로 절대값을 줘서 계산 후 반환 한다.
    return abs((date2 - date1).days)


if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
