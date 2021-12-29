import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan_array = []

for _ in range(k):
    lan_array.append(int(input()))

# print("lan_array : ", lan_array)

min_value = max(lan_array)

def binary_search(ary, target, start, end):
    if start > end:
        return target
    
    mid = (start + end) // 2

    count = 0
    # length = 0
    # print("mid : ", target, start, end, mid)

    for lan in ary:
        count += lan // mid

    # print("count : ", count)

    if count < n:
        return binary_search(ary, target, start, mid-1)
    else:
        return binary_search(ary, mid, mid+1, end)

print(binary_search(lan_array, 0, 1, min_value))