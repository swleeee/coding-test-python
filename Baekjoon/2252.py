from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    # print("indegree : ", indegree)

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    # print("q | graph : ", q, graph)
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)


    for i in result:
        print(i, end= ' ')

topology_sort()