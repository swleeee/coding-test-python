# 6095 : [기초-리스트] 바둑판에 흰 돌 놓기(설명)

list = []
for i in range(19):
    list.append([])
    for j in range(19):
        list[i].append(0)

n = int(input())
for i in range(n):
    x, y = map(int, input().split())    
    list[int(x-1)][int(y-1)] = 1

for i in range(19):
  for j in range(19): 
    print(list[i][j], end=' ')
  print() # 줄 바꿈    