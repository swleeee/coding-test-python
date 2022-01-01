# n = int(input())

# count = 1
# array = [1]
# dp = [1]
# types = [2, 3, 5]

# value = 2

# while count < n:
#     for type in types:
#         if value % type == 0:
#             if dp[(value // type) -1] == 1:
#                 dp.append(1)
#                 array.append(value)
#                 count += 1
#             else:
#                 dp.append(0)
#             break

#     if len(dp) != value:
#         dp.append(0)

#     value += 1

# # print("dp | array | count | answer : ", dp, array, count, array[count-1])
# print(array[count-1])

n = int(input())

ugly = [0] * n # 못생긴 수를 담기 위한 테이블 (1차원 DP 테이블)
ugly[0] = 1

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈값을 초기화
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수를 찾기
for l in range(1, n):
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
    ugly[l] = min(next2, next3, next5)

    print("before => l | next2 | next3 | next5 | ugly : ", l, next2, next3, next5, ugly)
    # 인덱스에 따라서 곱셈 결과를 증가
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

    print("\n")
    print("after => l | i2 | i3 | i5 | next2 | next3 | next5 | ugly : ", l, i2, i3, i5, next2, next3, next5, ugly)
    print("==========================================================")

# n번째 못생긴 수를 출력
print(ugly[n-1])