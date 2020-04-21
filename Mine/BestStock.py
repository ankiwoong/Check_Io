'''
Best Stock

You are given the current stock prices. You have to find out which stocks cost more.

Input:
The dictionary where the market identifier code is a key and the value is a stock price.

Output:
The market identifier code (ticker symbol) as a string.

Example:
best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"

Preconditions:
All the prices are unique.

def best_stock(data: dict) -> str:
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


def best_stock(data: dict):
    max_price = 0
    # answer 키
    answer = ''
    # data -> s(주식의 가격)
    for i in data:
        # max_price 보다 크면 대체
        if data[i] > max_price:
            max_price = data[i]
            answer = i

    # answer 반환
    return answer


if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    print("Coding complete? Click 'Check' to earn cool rewards!")
