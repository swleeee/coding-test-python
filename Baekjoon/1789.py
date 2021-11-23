sum = int(input())

n = 1

while True:    
    if(n <= sum):
        sum -= n
        n += 1        
    else:
        n -= 1
        break
print(n)