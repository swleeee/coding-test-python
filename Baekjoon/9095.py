import sys
input = sys.stdin.readline


t = int(input())
array = []
for _ in range(t):
    array.append(int(input()))

max_value = max(array)
d = [0] * (max_value + 1)

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, max_value + 1):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for s in array:
    print(d[s])