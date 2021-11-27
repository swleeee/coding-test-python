import sys
input = sys.stdin.readline

n = int(input())
ary = []
for i in range(n):
    ary.append(int(input()))

ary.sort()
# print(''.join(ary))
# print(ary)

for s in ary:
    print(s, sep="")