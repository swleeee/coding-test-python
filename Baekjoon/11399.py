n = int(input())
data = list(map(int, input().split()))
data.sort()
count = 0

for i in range(n):
    count += data[i] * (n-i)

print(count)