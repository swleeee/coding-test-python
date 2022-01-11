import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost

                heapq.heappush(q, (cost, i[0]))



dijkstra(1)

# print("distance : ", distance)

max_value = max(distance[1:])
count = 0
flag = True

for i in range(1, n+1):
    if distance[i] == max_value:
        if flag == True:
            print(i, end = " ")        
            flag = False
        count += 1
    
print(max_value, count)