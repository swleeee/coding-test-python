import heapq

# n = int(input())
# card = []
# for _ in range(n):
#     heapq.heappush(card, int(input()))
#     # card.append(int(input()))
    

# print("card : ", card)

# card.sort()

# count = 0
# for i in range(n-1):
#     n1 = heapq.heappop(card)
#     n2 = heapq.heappop(card)

#     count += n1 + n2
#     card.append(count)

# print(count)



# 10 20 30 40
# 10 + 20 + 30 + 30 + 60 + 40 = 190


### 풀이

n = int(input())

# Heap에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

# Heap에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)
