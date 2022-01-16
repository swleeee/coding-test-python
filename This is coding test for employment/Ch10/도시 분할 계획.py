def find_parent(parent, x):    
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):    
    a = find_parent(parent,a)
    b = find_parent(parent,b)    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 

v, e = map(int, input().split())
parent = [0] * (v+1) 

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())        
    edges.append((cost, a, b))

edges.sort()

max_value = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)        
        result += cost
        # if cost > max_value:
        #     max_value = cost
        max_value = cost

print(result)
print("max_value : ", max_value)
print(result - max_value)

### INPUT DATA
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4