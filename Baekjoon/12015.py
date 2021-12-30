import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

n = int(input())
array = list(map(int, input().split()))

part_array = []


def binary_search(ary, left_value, right_value):
    left_index = bisect_left(ary, left_value)
    right_index = bisect_right(ary, right_value)

    idx = right_index - left_index
    # print("DDDD : ", left_index)

    if idx > 0:
        return None
    else:
        return left_index
    

for data in array:
    if len(part_array) == 0 or part_array[len(part_array)-1] < data:
        part_array.append(data)
    else:
        value = binary_search(part_array, data, data) 
        if value != None:
            part_array[value] = data


# print("CCC : ", part_array)
print(len(part_array))




### 괜찮은 풀이
# import sys
# from bisect import bisect_left

# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
# DP = [0]

# for e in A:
#     if DP[-1] < e:
#         DP.append(e)
#     else:
#         index = bisect_left(DP, e)
#         DP[index] = e

# print(len(DP) - 1)