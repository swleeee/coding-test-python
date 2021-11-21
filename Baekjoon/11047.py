n, money = map(int, input().split())
ary = n * [0]
count = 0
for i in range(n):
    coin = int(input())
    ary[i] = coin

ary.sort(reverse=True)

for s in ary:
    if money == 0:
        break
    elif s > money:
        continue
    else:
        count += money // s
        money %= s

print(count)