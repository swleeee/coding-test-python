import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
data = []

for _ in range(n):
    data.append(list(map(str, input())))

# print(data)
# print(data[0][0])

# empty = []

# for i in range(n):
#     for j in range(m):
#         if data[i][j] == '.':
#             empty.append()

total_k = 0
total_v = 0
k = 0
v = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def count(x, y):
    global k 
    global v
    # global total_k
    # global total_v

    # print("data : ", data[x][y], data)

    if data[x][y] == 'k':
        k += 1
    elif data[x][y] == 'v':
        v += 1

    # print("k", x, y, v, k, data[x][y])

    data[x][y] = '#'
    # print("x y", x, y)
    for i in range(4):
    
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            # print("nx | ny | k | v | total_k | total_v", nx, ny, k, v, total_k, total_v)
            # print("nx", data)
            # if data[nx][ny] == '#':
            #     # print("#", nx, ny, k, v)
            #     continue
            # elif data[nx][ny] == 'k':
            #     k += 1
            #     data[nx][ny] = '#'
            #     # print("k", nx, ny, k, v)
            #     count(nx, ny, k, v)
            # elif data[nx][ny] == 'v':
            #     v += 1
            #     data[nx][ny] = '#'
            #     # print("v", nx, ny, k, v)
            #     count(nx, ny, k, v)
            # else:
            #     data[nx][ny] = '#'
            #     # print(".", nx, ny, k, v)
            #     count(nx, ny, k, v)
            if data[nx][ny] != '#':
                count(nx, ny)



def dfs():
    global total_k
    global total_v
    global k
    global v
    for i in range(n):
        for j in range(m):
            # print(i, j, total_k, total_v)
            if data[i][j] != '#':
                # print("i, j, k, v, total_k, total_v", i, j, k, v, total_k, total_v)                
                k = 0
                v = 0
                
                count(i, j)                                

                if k > v:
                    total_k += k
                else:
                    total_v += v

                # print("bbbbbbbbb", total_k, total_v)
                # print("count 후 : ", k, v, total_k, total_v)
                # k = 0
                # v = 0

dfs()
print(total_k, total_v)
                
