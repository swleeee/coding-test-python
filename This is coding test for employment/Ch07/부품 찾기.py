import sys
input = sys.stdin.readline

# n = int(input())
# parts = list(map(int, input().split()))
# m = int(input())
# estimate = list(map(int, input().split()))

# parts.sort()

# print("parts : ", parts)

# def binary_search(ary, target, start, end):
#     if start > end:
#         print("no", end = ' ')
#         return
    
#     mid = (start+end) // 2

#     if ary[mid] == target:
#         print("yes", end = ' ')
#         return
#     elif ary[mid] > target:
#         binary_search(ary, target, start, mid-1)
#     else:
#         binary_search(ary, target, mid+1, end)


# for part in estimate:
#     binary_search(parts, part, 0, n-1)



### 풀이1 (이진 탐색)
# 이진 탐색 소스코드 구현(반복문)
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start+end)//2

#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1

#         else:
#             start = mid + 1
#     return None

# n = int(input())
# array = list(map(int, input().split()))
# array.sort()
# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     result = binary_search(array, i, 0, n-1)
#     if result != None:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')



### 풀이2 (계수 정렬)
# n = int(input())
# array = [0] * 1000001

# # 가게에 있는 전체 부품 번호를 입력받아서 기록
# for i in input().split():
#     array[int(i)] = 1

# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')


### 풀이3 (집합 자료형 이용)
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')


### Input Data
# 5
# 8 3 7 9 2
# 3 
# 5 7 9