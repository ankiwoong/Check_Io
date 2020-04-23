'''
Domino Chain

You have a Domino box. Domino tiles contain two numbers from 0 (empty) to 6. Tiles are unordered and 1-6 is the same as 6-1. The double-six set contains 28 unique tiles - all combinations of number pairs.

Several tiles fell out of the box. You should try to line up a chain from these tiles, compiling them to each other's suitable sides (sides with the same numbers). Thus, you can get a continuous chain of tiles. In some cases, such a chain will not be the only one.

For example, you've ended up these tiles:
1-5, 2-5, 3-5, 4-5, 3-4
So, with them you can build two complete chains:
1-5, 5-3, 3-4, 4-5, 5-2
1-5, 5-4, 4-3, 3-5, 5-2
Your goal in this mission is to count how many complete chains you can make using all of the given dominoes.

Note. Chains must be unique. An inverted chain is not considered as unique: "1-2, 2-3, 3-4, 4-5" and "5-4, 4-3, 3-2, 2-1" are the same chain.

Input:
String with the description of the domino tiles. Like this one: "5-4, 4-3, 3-2, 2-1".

Output:
Integer. The maximum number of complete chains that you can build using all of the given tiles.

Examples:
domino_chain("0-2, 0-5, 1-5, 1-3, 5-5") == 1
domino_chain("1-5, 2-5, 3-5, 4-5, 3-4") == 2
domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4") == 0

How it is used:
This is a combinatorial problem. You can solve it by modeling a real game of dominoes. Or refreshing your knowledge of graph theory. Many things in life resemble the process of forming a domino chain: for example, flights between several cities.

Precondition:
5 <= len(given_tiles) <= 17


def domino_chain(tiles: str) -> int:
    # your code here
    return 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert domino_chain("0-2, 0-5, 1-5, 1-3, 5-5") == 1
    assert domino_chain("1-5, 2-5, 3-5, 4-5, 3-4") == 2
    assert domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4") == 0
    assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4") == 6
    assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4, 3-0, 0-4") == 0
    assert domino_chain("1-2, 2-2, 2-3, 3-3, 3-1") == 5
    assert domino_chain("1-4, 3-4, 0-4, 0-5, 4-5, 2-4, 2-5") == 0
    assert domino_chain("1-4, 1-5, 0-2, 1-6, 4-6, 4-5, 5-6") == 0
    assert domino_chain("1-2, 2-3, 2-4, 3-4, 2-5, 2-6, 5-6") == 8
    assert domino_chain("1-2, 2-3, 3-1, 4-5, 5-6, 6-4") == 0
    assert domino_chain("1-2, 1-4, 1-5, 1-6, 1-1, 2-5, 4-6") == 28
    print("Basic tests passed.")
'''


from collections import defaultdict
from collections import namedtuple


def domino_chain(tiles: str):
    # 주어진 타일에서 형성된 고유 한 도미노 체인 수를 반환
    Domino = namedtuple('Domino', 'tile other_side')

    pips = defaultdict(list)
    tile_list = [(int(t[0]), int(t[2])) for t in tiles.split(', ')]

    # pips를 키로 사용하고 tile를 사용하여 딕셔너리를 작성
    # 값으로 일치하는 pips를 변수에 추가
    for _idx, tile in enumerate(tile_list):
        pips[tile[0]].append(Domino(tile, tile[1]))
        if tile[0] != tile[1]:
            pips[tile[1]].append(Domino(tile, tile[0]))

    tiles_len = len(tile_list)

    # 가능한 모든 조합을 찾기위한 너비 우선 탐색 기능 알고리즘
    # 주어진 tile와 그 tile의 한쪽에있는 pips로 시작
    def find_all_paths(start_tile, pip_value, path=[]):
        path = path + [start_tile]

        # 모든 tile이 사용되면 종료 후 반환
        if len(path) == tiles_len:
            return [path]

        paths = []
        for domino in pips[pip_value]:
            if domino.tile not in path:
                newpaths = find_all_paths(domino.tile, domino.other_side, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    # 모든 tiles의 한쪽을 사용하여 모든 경로를 찾은 다음
    # 각 타일의 다른 쪽을 검색.
    all_paths = []
    for tile in tile_list:
        paths = find_all_paths(tile, tile[1])
        if paths:
            all_paths.extend(paths)
        if tile[0] != tile[1]:
            paths = find_all_paths(tile, tile[0])
            if paths:
                all_paths.extend(paths)

    # 각 경로의 미러 이미지가 결과에 포함되므로 최종 카운트를 반으로 줄입니다.
    return len(all_paths) // 2


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert domino_chain("0-2, 0-5, 1-5, 1-3, 5-5") == 1
    assert domino_chain("1-5, 2-5, 3-5, 4-5, 3-4") == 2
    assert domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4") == 0
    assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4") == 6
    assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4, 3-0, 0-4") == 0
    assert domino_chain("1-2, 2-2, 2-3, 3-3, 3-1") == 5
    assert domino_chain("1-4, 3-4, 0-4, 0-5, 4-5, 2-4, 2-5") == 0
    assert domino_chain("1-4, 1-5, 0-2, 1-6, 4-6, 4-5, 5-6") == 0
    assert domino_chain("1-2, 2-3, 2-4, 3-4, 2-5, 2-6, 5-6") == 8
    assert domino_chain("1-2, 2-3, 3-1, 4-5, 5-6, 6-4") == 0
    assert domino_chain("1-2, 1-4, 1-5, 1-6, 1-1, 2-5, 4-6") == 28
    print("Basic tests passed.")
