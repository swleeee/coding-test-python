# 6098 : [기초-리스트] 성실한 개미


list = []

for i in range(10):
    list.append([])
    for j in range(10):
        list[i].append(0)


for i in range(10):     
    a = input().split() 
    for j in range(10):         
        list[i][j] = int(a[j])

x=1
y=1

while 1:
    # print("a")    
    if((x==9 and y==9) or (list[x][y]== 2)):        
        list[x][y] = 9
        break    
    list[x][y] = 9
    if(list[x][y+1] != 1):
        y += 1    
    else:
        if(list[x+1][y]!=1):
            x +=1        
        else:
            break

# print("==========================")

for i in range(10):
  for j in range(10): 
    print(list[i][j], end=' ')
  print() # 줄 바꿈    