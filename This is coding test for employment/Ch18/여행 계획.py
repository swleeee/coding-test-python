def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

for i in range(1, n+1):
    print("find_parent : ", find_parent(parent, i))

plans = set(map(int, input().split()))

print("plans : ", plans)

std_route = find_parent(parent, list(plans)[0])
flag = True
for plan in plans:    
    route = find_parent(parent, plan)
    if std_route != route:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
### INPUT DATA
# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0 
# 2 3 4 3