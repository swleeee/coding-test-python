INF = int(1e9)
import heapq

def dijkstra(distance, start, graph):
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


def solution(n, edge):
    answer = 0    
    graph = [[] for _ in range(n+1)]    
    distance = [INF] * (n+1)
    for v in edge:
        graph[v[0]].append((v[1], 1))
        graph[v[1]].append((v[0], 1))
        
        
    dijkstra(distance, 1, graph)
    print("distance : ", distance)
    max_value = max(distance[1:])
    print("max_value : ", max_value)
    answer = distance.count(max_value)
    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))