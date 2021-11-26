x, y = map(int, input().split())

count = 0
if (x == 1):    
    count = 1
elif (x == 2):    
    count = min(4, (y+1) // 2)
else:
    if(y<=4):
        count = y
    elif(y<=7):
        count = (y+1)//2 + 1
    else:
        count = y-2

print(count)