from collections import deque
import copy
import sys
input = sys.stdin.readline

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]

    if data[1]:
        for x in data[2:]:
            graph[x].append(i)
            indegree[i] += 1

# print("graph : ", graph)
def topology_sort():
    q = deque()
    result = copy.deepcopy(time) 

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        # print("q : ", q)
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            # print("graph[now] : ", graph[now])
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    
    print("result : ", result)

    print(max(result[1:n+1]))


topology_sort()


