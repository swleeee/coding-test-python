import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
q = []
# heapq.heappush(q, list(map(int, input().split())))
cards = list(map(int, input().split()))


for card in cards:
    heapq.heappush(q, card)
# print("q : ", q)

for i in range(m):
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    c = a+b
    for _ in range(2):
        heapq.heappush(q, c)
    
print(sum(q))
    