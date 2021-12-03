import sys
input = sys.stdin.readline
from collections import deque

# # count = 0
# answer = []
# # isExist = False

# def dfs(graph, v, visited, minV, count = 0):
#     print("a", v, visited, count)
#     visited[v] = True
#     count += 1
#     for i in graph[v]:
#         if not visited[i-1]:
#             if temp[i-1] == 0:
#                 temp[i-1] = count
#             if(minV == count):             
#                 print("t", temp)            
#                 if(temp[i-1] == count):
#                     answer.append(str(i))                        
#             else:
                
#                 dfs(graph, i-1, visited, K, count)
            

# N, M, K, X = map(int, input().split())

# graph = [[] for _ in range(N)]
# temp = [0 for _ in range(N)]
# data = []

# for _ in range(M):
#     data = list(map(int, input().split()))
#     graph[data[0]-1].append(data[1])
#     print(data)

# print(graph)

# visited = [False] * N

# dfs(graph, X-1, visited, K)

# print(answer)
# print(temp)



### 풀이
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

q = deque([x])
while q:    
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        print("q", q, now, graph, distance)
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now]+1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)