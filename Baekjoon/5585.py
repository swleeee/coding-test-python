n = int(input())
coin_type=[500, 100, 50, 10, 5, 1]
n = 1000-n
count = 0

for coin in coin_type:
    if(n >= coin):
        count += n//coin
        n %= coin
    if(n==0):
        break

print(count)



