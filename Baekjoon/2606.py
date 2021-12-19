import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
k = int(input())

graph=[[] for _ in range(n+1)]



visited = [False] * n

for i in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print("graph : ", graph)

result = []

def bfs(graph, start, visited):
    q = deque([start])

    visited[start-1] = True

    while q:
        now = q.popleft()
        print("now | q : ", now, q)
        for i in graph[now]:
            if not visited[i-1]:
                q.append(i)
                visited[i-1] = True
                if i not in result:
                    result.append(i)

bfs(graph, 1, visited)

# print("result : ", result, len(result))
print("visited : ", visited, result)
print(len(result))
