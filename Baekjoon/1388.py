from collections import deque
import sys
input = sys.stdin.readline

# N, M = map(int, input().split())

# graph = [input() for _ in range(N)]
# data = [[-1] * M for _ in range(N)]

# # print(graph)



# def dfs(x, y, prev_value):
#     # global count 
#     # q = deque()
#     # q.append((0,0))
    

#     # if ( x== 0 and y==0):
#     #     prev_value=''

#     if(x >= N or y>=M):
#         return
#     # print("dd", x+1, y+1, prev_value, data[x])
#     # print("dd", x+1, y+1, prev_value, count)

#     if graph[x][y] == '-':
#         # print("e")
#         if(prev_value == '-'):
#             graph[x][y].replace('-', '0')
#             data[x][y] = 0
#             dfs(x, y+1, '-')
#         elif(prev_value == '|'):
#             graph[x][y].replace('-', '1')
#             # if(data[x][y] == -1):
#                 # data[x][y] = 1
#                 # count += 1
#             # dfs(x, y+1, '-')        
#         else:
#             graph[x].replace('-', '1')
#             data[x][y] = 1
#             # count += 1
#             # print("g", graph[x][y])
#             dfs(x, y+1, '-')    
#     else:
#         if(prev_value == '-'):
#             graph[x][y].replace('|', '1')
#             # if(data[x][y] == -1):
#                 # count += 1
#                 # data[x][y] = 1
#             # dfs(x+1, y, '|')
#         elif(prev_value == '|'):
#             graph[x][y].replace('|', '0')    
#             data[x][y] = 0
#             dfs(x+1, y, '|')    
#         else:
#             graph[x][y].replace('|', '1')
#             data[x][y] = 1
#             # count += 1
#             dfs(x+1, y, '|')    


# count = 0
# for i in range(N):
#     for j in range(M):      
#         # print("aaaaaa", i+1, j+1, data)  
#         if data[i][j] == -1:
#             dfs(i, j, '')


# for i in range(N):
#     for j in range(M):
#         if data[i][j] == 1:
#             count+= 1
# # print("data", data)
# # print("graph", graph)
# # print("count", count)
# print(count)

# for s in graph:
#     for sub_s in s:
#         print("sub_s", sub_s)






### 풀이1
# N, M = map(int, input().split())
# floor = [list(input()) for _ in range(N)]
# ans = 0
# for i in range(N):
#     cng = '.'
#     for j in range(M):
#         if floor[i][j] == '-':
#             if floor[i][j] != cng:
#                 ans += 1
#         cng = floor[i][j]
# for i in range(M):
#     cng = '.'
#     for j in range(N):
#         if floor[j][i] == '|':
#             if floor[j][i] != cng:
#                 ans += 1
#         cng = floor[j][i]
# print(ans)


### 풀이2
# from collections import deque

n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
queue = deque()

cnt = 0

for i in range(n):
    for j in range(m):        
        if not visited[i][j]:
            queue.append(arr[i][j])
            a = i
            b = j
            print("queue", i, j, queue, cnt)
            while queue:
                visited[a][b] = True
                s = queue.popleft()
                if s == '-' and b + 1 < m:
                    if s == arr[a][b + 1]:
                        b += 1
                        queue.append(arr[a][b])
                elif s == '|' and a + 1 < n:
                    if s == arr[a + 1][b]:
                        a += 1
                        queue.append(arr[a][b])
            cnt += 1

print(cnt)