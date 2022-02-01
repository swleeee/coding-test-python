import heapq
from collections import deque

def solution(operations):
    # answer = []
    max_q = []
    min_q = []
    operations = deque(operations)
    while operations:
        operation = operations.popleft().split()
        print("operation : ", operation)
        
        if operation[0] == "I":
            heapq.heappush(min_q, int(operation[1]))
            heapq.heappush(max_q, -int(operation[1]))
            # print("a : ", q)
        elif len(min_q) == 0:
            continue
        else:
            if operation[1] == '1':
                heapq.heappop(max_q)  
                min_q.pop()              
            else:
                heapq.heappop(min_q)
                max_q.pop()
    # print("operations : ", operations)
        print("q : ", min_q, max_q)
        print()
    if len(min_q) > 0:
        return [-max_q[0], min_q[0]]
    else:
        return [0, 0]
    # return answer

# operations = ["I 7","I 5","I -5","D -1"]
# operations = ["I 16","D -1"]
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))