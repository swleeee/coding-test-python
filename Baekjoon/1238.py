import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph_A = [[] for _ in range(n+1)]
graph_B = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance_A = [INF] * (n+1)
distance_B = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph_A[a].append((b, c))
    graph_B[b].append((a, c))


def dijkstra(start, distance, graph):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # print("before : ", q)
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

        # print("after : ", distance)
        


dijkstra(start, distance_A, graph_A)
visited = [False] * (n+1)
dijkstra(start, distance_B, graph_B)

max_value = -1
for i in range(1, n+1):
    max_value = max(max_value, distance_A[i] + distance_B[i])
    # print(distance_A[i])


print(max_value)