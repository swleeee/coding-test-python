n = int(input())
data = [int(input()) for _ in range(n)]

print("data : ", data)

ary = sorted(data, reverse=True)

for s in ary:
    print(s, end=" ")