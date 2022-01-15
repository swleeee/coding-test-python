import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]

# move_list = [0] * (v+1)


for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start, start))
    distance[start] = 0

    first_route = start

    while q:
        dist, now, prev = heapq.heappop(q)

        if distance[now] < dist:
            continue

        # print("(before) move_list | now | prev | start : ", move_list, now, prev, start)
        if move_list[now] == now and start != prev:
            move_list[now] = prev

        if now == prev or prev == start:
            next = now
        else:
            next = prev

        # print("(after) move_list | now | prev | start | next : ", move_list, now, prev, start, next)
        # print()

        for i in graph[now]:
            
            cost = dist + i[1]
            

            if cost < distance[i[0]]:                
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0], next))

                # if first_route == now:
                #     move_list[i[0]] = i[0]
                # else:
                #     move_list[i[0]] = i[0]
            # print("q : ", q)
        # print()

for i in range(1, v+1):
    move_list = [i for i in range(v+1)]
    distance = [INF] * (v+1)
    dijkstra(i)

    for j in range(1, v+1):
        # if distance[j] == INF:
        #     print(0, end=" ")
        if i == j:
            print("-", end=' ')
        else:
            # print(distance[j], end=' ')
            print(move_list[j], end= ' ')
        
    print()

# print("move_list : ", move_list[1:])