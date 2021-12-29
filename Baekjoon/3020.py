import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

n, h = map(int, input().split())
# cave = [0] * h
bottom = []
top = []

for i in range(n):
    block = int(input())
    if i % 2 == 0:
        bottom.append(block)
    else:
        top.append(block)



top.sort()
bottom.sort()

# print("top : ", top)
# print("bottom : ", bottom)

min_value = n+1
total_count = 0
top_total_count = sum(top)
bottom_total_count = sum(bottom)


def binary_search(type, ary, left_value, total_count):
    global bottom_total_count
    global top_total_count

    left_index = bisect_left(ary, left_value)
    # right_index = bisect_right(ary, right_value)
    # print("left_index | total_count : ", left_index, total_count)
    # total_count -= n//2 - left_index
    # return right_index - left_index
    if type == "bottom":
        bottom_total_count -= n//2 - left_index
    else:
        top_total_count -= n//2 - left_index
    return n//2 - left_index

for i in range(1, h+1):
    bottom_count = binary_search("bottom", bottom, i, bottom_total_count)
    top_count = binary_search("top", top, h-i+1, top_total_count)
    # print("BBB : ", bottom_count + top_count, min_value, total_count)
    if bottom_count + top_count < min_value:
        min_value = bottom_count + top_count
        total_count = 1
    elif bottom_count + top_count == min_value:
        total_count += 1

print(min_value, total_count)
    