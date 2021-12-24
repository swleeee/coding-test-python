import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a+b
# print("c : ", c)


c.sort()

for num in c:
    print(num, end=' ')


### print(" ".join(map(str, c)))