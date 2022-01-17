from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    data = list(map(int, input().split()))
    a = data[1]

    for x in data[2:]:
        # print("aaa : ", a, x)
        graph[a].append(x)
        indegree[x] += 1
        a = x

def topology_sort():
    q = deque()
    result = []

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    # print("graph : ", graph, indegree)
    
    while q:
        # print("q : ", q)
        now = q.popleft()
        result.append(now)
        # print("now : ", now, graph[now])

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

        # if len(q) == 0:
        #     print(0)
        #     break

    if len(result) == n:
        for i in result:
            print(i)
    else:
        print(0)

topology_sort()