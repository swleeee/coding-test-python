from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# parts = [-1] * (n+1)
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
costs = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    mid, basic, count = map(int, input().split())
    graph[basic].append((mid, count))
    indegree[mid] += 1
    # costs[mid].append((basic, count))

# print("costs : " , costs) 
# print("indegree : " , indegree) 
# print("graph : " , graph) 


def topology_sort():
    q = deque()
    # result = []
    answer = []

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            # answer.append(i)
            # parts[i] = 0

    # print("parts : ", parts)
    # print("answer : ", answer)
    while q:
        # print("q : ", q)
        now = q.popleft()
        # result.append(now)

        for i, count in graph[now]:

            if costs[now].count(0) == n+1:
                costs[i][now] += count
            else:
                for j in range(1, n+1):
                    costs[i][j] += costs[now][j] * count
            indegree[i] -= 1            
            # parts[i].append(())
            if indegree[i] == 0:
                q.append(i)

        # for cost in costs[now]:
        #     a, b = cost
        #     if a < 5:
        #         parts[a] += b
            
    # print("result : " , result) 
    # print("ddd : ", costs)
    for i in range(1, n+1):
        if costs[n][i] != 0:
            print(i, costs[n][i])

    # for x in enumerate(costs[n]):
    #     if x[1] > 0:
    #         print(*x)

    
topology_sort()