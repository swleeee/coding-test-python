import sys
input = sys.stdin.readline

n = int(input())
ary=[]

for i in range(n):
    ary.append(int(input()))
    
ary.sort()

for i in range(n):
    ary[i] *= (n-i)

print(max(ary))