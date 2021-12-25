import sys
input = sys.stdin.readline

# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort(reverse=True)

# def binary_search(array, target, start, end):
    

#     mid = (start + end) // 2


    
#     if start > end or mid == 0:        
#         return

#     count = 0



#     for i in range(mid):
#         count += (abs(array[mid] - array[i]))

#     print("mid : ", mid, count, target)

#     if count == target:
#         # print("aaa", array[mid])
#         print(array[mid])
#         return
#     elif count > target:
#         binary_search(array, target, start, mid-1)        
#     else:
#         binary_search(array, target, mid+1, end)


# binary_search(data, m, 0, n-1)


### 풀이
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1

    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)




### Input Data
# 19 17 15 10
# 2 2

# 4 6
# 19 15 10 17

# 19 17 14 10

# 4 6
# 19 14 10 17