'''
Disposable Teleports

The island has eight stations which are connected by a network of teleports; however, the teleports take a very long time to recharge. This means you can only use each one once. After you use a teleport, it will shut down and no longer function. But you can visit any station more than once. For this task, you should begin at number 1 and try to travel around to all the stations before returning to the starting point. The map of the teleports is presented as a string in which the comma-separated list represents teleports. Each teleport is given the name of the station it connects to. This name consists of two digits, such as '12' or '32.' Each test requires you to provide a route which passes through every station. A route is presented as a string of the station numbers in the sequence in which they must be visited (ex. 123456781).

disposable-teleports

Input:
A teleport map as a string.

Output:
The sequence of station numbers as a string.

Example:
checkio("12,23,34,45,56,67,78,81") == "123456781"
checkio("12,28,87,71,13,14,34,35,45,46,63,65") == "1365417821"
checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") == "12382478561"
checkio("13,14,23,25,34,35,47,56,58,76,68") == "132586741"

How it is used:
This task is another example of the graph-search problem. It’s like trying to find a route where you can not to step on the same spot twice.

Precondition:
len(stations) == 8
Teleports are not repeated and undirected.


def checkio(teleports_string):
    #return any route from 1 to 1 over all points

    return "123456781"

#This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"
'''


def checkio(teleports_string):
    # 이 함수는 텔레포트 그래프 내부의 경로를 찾으려고 시도합니다.
    # https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html
    # 너비 우선 탐색 알고리즘을 사용합니다.
    # 텔레 포터 연결 목록 작성
    ways = [string for string in teleports_string.split(',')]
    results = ['1']
    # 올바른 방법을 찾을 때까지 그래프에서 새로운 방법 찾기
    while not any(all(str(w) in res for w in range(1, 9)) and res[-1] == '1'
                  for res in results):
        new_results = []
        # 결과로 모든 항목을 시도합니다.
        for item in results:
            # 아이템에 더 많은 노드를 추가하려고 합니다.
            for i in range(1, 9):
                end = item[-1] + str(i)
                # 텔레포트가 존재하고 사용되지 않아야합니다
                if ((end in ways or end[::-1] in ways) and end not in item and
                        end[::-1] not in item):
                    new_results += [item + str(i)]
        # 결과를 새로운 결과로 변경
        results = new_results[:]
    # 최종 결과 찾기
    for result in results:
        if all(str(w) in result for w in range(1, 9)) and result[-1] == '1':
            return result


# This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)]))
                         for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(
        checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(
        checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(
        checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"
