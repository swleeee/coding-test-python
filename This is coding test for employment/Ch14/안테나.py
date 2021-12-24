# n = int(input())
# house = list(map(int, input().split()))

# print("house : ", house)

# house.sort()

# pivot = 0
# total_value= 0
# idx = 0

# def calc_loc(pivot):
#     total = 0
#     for i in range(n):
#         total += abs(house[pivot] - house[i])
#     print("total: ", total, pivot, house)
#     return total

# if n % 2 == 0:
#     total_value = min(calc_loc(n//2), calc_loc(n//2 - 1))
#     if calc_loc(n//2) < calc_loc(n//2 -1 ):
#         idx = n//2
#     else:
#         idx = n//2 -1
# else:
#     # pivot = house[n//2]
#     # pivot = n//2
#     # total_value = calc_loc(n//2)
#     idx = n//2

# print(house[idx])



### 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

# 중간값(median)을 출력
print(data[(n-1)//2])