import sys
input = sys.stdin.readline
import heapq

n = int(input())
ary = []
for i in range(n):
    # ary.append(int(input()))
    heapq.heappush(ary, int(input()))

# print(ary)
ary.sort()

count = 0
for i in range(n-1):
    # print(heapq.heappop(ary))
    a = heapq.heappop(ary)
    b = heapq.heappop(ary)
    count += a + b
    ary.append(a + b) # heapq.heappush(ary, a+b)
    # # print("ary 전", ary)
    # del ary[0]
    # del ary[0]
    # # ary.sort()
    # # print("ary 후", ary)

print(count)