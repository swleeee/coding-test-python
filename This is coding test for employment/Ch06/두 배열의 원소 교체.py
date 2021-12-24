
# n, k = map(int, input().split())

# ary_A = list(map(int, input().split()))
# ary_B = list(map(int, input().split()))

# print(ary_A, ary_B)

# def quick_sort(ary):
#     if len(ary) <= 1:
#         return ary

#     pivot = ary[0]
#     tail = ary[1:]

#     left_ary = [x for x in tail if x <= pivot]
#     right_ary = [x for x in tail if x > pivot]

#     return quick_sort(left_ary) + [pivot] + quick_sort(right_ary)

# ary_A = quick_sort(ary_A)
# ary_B = quick_sort(ary_B)


# print(ary_A)
# print(ary_B)

# for i in range(k):
#     ary_A[i], ary_B[n-i-1] = ary_B[n-i-1], ary_A[i]


# result = 0

# for num in ary_A:
#     result += num

# print(result)




### 풀이
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))