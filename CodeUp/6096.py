# 6096 : [기초-리스트] 바둑알 십자 뒤집기

list = []
for i in range(19):
    list.append([])
    for j in range(19):
        list[i].append(0)

for i in range(19): 
    a = input().split() 
    for j in range(19): 
        list[i][j] = int(a[j])




n = int(input())
for i in range(n):
    x, y = map(int, input().split())    
    for j in range(19):
        if list[j][int(y-1)]==0:
            list[j][int(y-1)]=1
        else :
            list[j][int(y-1)]=0

        if list[int(x-1)][j]==0:
            list[int(x-1)][j]=1
        else :
            list[int(x-1)][j]=0
    

for i in range(19):
  for j in range(19): 
    print(list[i][j], end=' ')
  print() # 줄 바꿈    