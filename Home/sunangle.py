'''
Sun Angle

Every true traveler must know how to do 3 things: fix the fire, find the water and extract useful information from the nature around him. Programming won't help you with the fire and water, but when it comes to the information extraction - it might be just the thing you need.

Your task is to find the angle of the sun above the horizon knowing the time of the day. Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees. If the input will be the time of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!".

example

Input: 
The time of the day.

Output:
The angle of the sun, rounded to 2 decimal places.

Example:
sun_angle("07:00") == 15
sun_angle("12:15"] == 93.75
sun_angle("01:23") == "I don't see the sun!"

How it is used:
One day it can save your life, if you'll be lost far away from civilization.

Precondition:
00:00 <= time <= 23:59

def sun_angle(time):
    #replace this for solution
    return time

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


def sun_angle(time):
    # 시간 문자열을 시간과 분으로 나눕니다.
    # 시간 추출 :을 기준으로 나눠서 0번 인덱스
    h = int(time.split(':')[0])
    # 분 추출 : 을 기준으로 나눠서 1번 인덱스
    m = int(time.split(':')[1])
    # 1 시간은 15 °, 1 분은 0.25 °에 해당한다.
    # 각도를 계산하고 합산하십시오.
    angle = (h - 6) * 15 + m * 0.25
    # 변수 범위 반정 후 반환
    if 0 <= angle <= 180:
        return angle
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
