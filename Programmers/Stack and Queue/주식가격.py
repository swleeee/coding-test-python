from collections import deque

def solution(prices):
    answer = []
    times = deque()
    while prices:
        print("prices : ", prices, times)
        price = prices.pop()
        count = 0
        for i, time in enumerate(times):
            count += 1
            if price > time:
                break
        
        print("count : ", count)
        times.appendleft(price)
        answer.append(count)
        print()
    
    print("answer : ", answer)

    answer.reverse()
    return answer

prices = [1, 2, 3, 2, 3] 
## [4, 3, 1, 1, 0]

prices = [1, 2, 3, 2, 3, 1] 
## [5, 4, 1, 2, 1, 0]


print(solution(prices))