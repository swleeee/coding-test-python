### 1) 정답 (서로소 집합 알고리즘)
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# def solution(n, computers):
#     parent = [0] * (n+1)
#     for i in range(1, n+1):
#         parent[i] = i

#     for i in range(n):
#         for j in range(i, n):
#             if computers[i][j] == 1 and i != j:
#                 union_parent(parent, i+1, j+1)

#     # answer = 0
#     print("parent : ", parent)
#     print(len(set(parent[1:])))
#     answer = set()
#     for i in range(n):
#         parent[i] = find_parent(parent, i);
#         answer.add(parent[i]);

#     return len(answer)
#     # return len(set(parent[1:]))


### 2) 다른 사람 풀이 1 BFS 같은 DFS..?
# def solution(n, computers):
#     answer = 0
#     visited = [0 for i in range(n)]
#     def dfs(computers, visited, start):
#         print("computers : ", computers)
#         print("visited : ", visited)
#         print("start : ", start)
#         stack = [start]
#         while stack:
#             print("stack : ", stack)
#             j = stack.pop()
#             if visited[j] == 0:
#                 visited[j] = 1
#             # for i in range(len(computers)-1, -1, -1):
#             for i in range(0, len(computers)):
#                 if computers[j][i] ==1 and visited[i] == 0:
#                     stack.append(i)
#     i=0
#     while 0 in visited:
#         if visited[i] ==0:
#             dfs(computers, visited, i)
#             answer +=1
#         i+=1
#     return answer

### 3) 다른 사람 풀이2 deque가 아닌 그냥 리스트? BFS
def solution(n, computers):    
    def BFS(node, visit):
        que = [node]
        visit[node] = 1
        while que:
            v = que.pop(0)
            for i in range(n):
                if computers[v][i] == 1 and visit[i] == 0:
                    visit[i] = 1
                    que.append(i)
        return visit
    visit = [0 for i in range(n)]
    answer = 0
    for i in range(n):
        try:
            visit = BFS(visit.index(0), visit)
            answer += 1
        except:
            break
    return answer



n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
## 2

# n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
## 1

print(solution(n, computers))