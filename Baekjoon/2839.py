n = int(input())
count = 0

while True:
    if(n==0):
        break
    if(n < 0):
        count = -1
        break
    if(n%5==0):
        count += n//5
        break
    else:
        count += 1
        n -= 3
print(count)
