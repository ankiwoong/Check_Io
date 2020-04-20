'''
Find Sequence


“There’s nothing here...” sighed Nikola.

“You’re kidding right? All treasure is buried treasure! It wouldn’t be treasure otherwise!” Said

Sofia. “Here, take these.” She produced three shovels from a backpack that seemed to appear out of thin air.

“Where did you get-”

“Don’t ask questions. Just dig!” She hopped on the shovel and began digging furiously.

CLUNK

“Hey we hit something.” Stephen exclaimed in surprise.

“It’s the treasure!” Sofia was jumping up and down in excitement.

The trio dug around the treasure chest and pulled it out of the hole and wiped the dirt off. Sofia tried grabbing the lid but it was locked. Nikola studied the locking mechanism.

“I’ve seen this type of lock before. It’s pretty simple. We just need to check whether there is a sequence of 4 or more matching numbers and output a bool.”

“Easy enough. Let’s open this sucker up!” Sofia was shaking in excitement.

You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

find-sequence

Input:
A matrix as a list of lists with integers.

Output:
Whether or not a sequence exists as a boolean.

Example:
checkio([
    [1, 2, 1, 1],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5]
]) == True
checkio([
    [7, 1, 4, 1],
    [1, 2, 5, 2],
    [3, 4, 1, 3],
    [1, 1, 8, 1]
]) == False
checkio([
    [2, 1, 1, 6, 1],
    [1, 3, 2, 1, 1],
    [4, 1, 1, 3, 1],
    [5, 5, 5, 5, 5],
    [1, 1, 3, 1, 1]
]) == True
checkio([
    [7, 1, 1, 8, 1, 1],
    [1, 1, 7, 3, 1, 5],
    [2, 3, 1, 2, 5, 1],
    [1, 1, 1, 5, 1, 4],
    [4, 6, 5, 1, 3, 1],
    [1, 1, 9, 1, 2, 1]
    ]) == True

How it is used:
This concept is useful for games where you need to detect various lines of the same elements (match 3 games for example). This algorithm can be used for basic pattern recognition.

Precondition:
0 ≤ len(matrix) ≤ 10
all(all(0 < x < 10 for x in row) for row in matrix)


def checkio(matrix):
    #replace this for solution
    return True or False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
'''
# Case1


from itertools import groupby


def checkio(matrix):
    # 행
    for row in matrix:
        for start in range(0, len(row)-3):
            if len(set(row[start:start + 4])) == 1:
                return True

    # 열
    for column in range(len(matrix[0])):
        list = []
        for row in range(len(matrix)):
            list.append(matrix[row][column])
        for start in range(0, len(list)-3):
            if len(set(list[start:start + 4])) == 1:
                return True

    # 대각선 아래
    for row in range(4-len(matrix), len(matrix)-3):
        list = []
        for column in range(len(matrix)):
            if row+column in range(len(matrix)):
                list.append(matrix[row+column][column])
        for start in range(0, len(list)-3):
            if len(set(list[start:start + 4])) == 1:
                return True

    # 대각선 위
    for row in range(3, 2*len(matrix)-4):
        list = []
        for column in range(len(matrix)):
            if row-column in range(len(matrix)):
                list.append(matrix[row-column][column])
        for start in range(0, len(list)-3):
            if len(set(list[start:start + 4])) == 1:
                return True

    return False


# Case 2


def has_n_seq(l, n):
    # 목록 'l'에 일련의 'n'이상의 일치 숫자가 있으면 True, 그렇지 않으면 False
    if len(l) > 0:
        return max(len(list(g)) for _, g in groupby(l)) >= n
    else:
        return False


def checkio2(matrix):
    # 행
    for row in matrix:
        if has_n_seq(row, 4):
            return True

    # 열
    for col in zip(*matrix):
        if has_n_seq(col, 4):
            return True

    # 대각선
    n = len(matrix)
    for p in range(2*n-1):
        # 참고 : https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
        # 왼쪽 아래 오른쪽 위 대각선 확인
        if has_n_seq([matrix[p-q][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)], 4):
            return True
        # 왼쪽 상단에서 오른쪽 하단 대각선 확인
        if has_n_seq([matrix[n-p+q-1][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)], 4):
            return True

    # 아무것도 찾을 수 없음
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio2([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio2([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio2([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio2([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
