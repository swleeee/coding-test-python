# 6097 : [기초-리스트] 설탕과자 뽑기

h, w = map(int, input().split())
list = []

for i in range(h):
    list.append([])
    for j in range(w):
        list[i].append(0)

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    if(d==0):
        for j in range(l):
            list[x-1][y+j-1] = 1
    else:
        for j in range(l):
            list[x+j-1][y-1] = 1


for i in range(h):
  for j in range(w): 
    print(list[i][j], end=' ')
  print() # 줄 바꿈    