# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# array = list(map(int, input().split()))
# max_value = sum(array)

# def binary_search(ary, target, start, end):
#     if start > end:
#         return target
    
#     mid = (start+end)//2

#     max_value = 0
#     value = 0
#     count = 1

#     for i in range(n):
#         value += ary[i]
#         if value > mid:
#             count += 1
#             value -= ary[i] 
#             max_value = max(max_value, value)
#             value = ary[i]    
#             # print("bbb : ", i, max_value)
#             if i == n-1:
#                 max_value = max(max_value, value)
#         else:
#             max_value = max(max_value, value)
        
    
            
#     # print("AAA : ", start, end, mid, count, max_value)

#     if count <= m:
#         return binary_search(ary, max_value, start, mid-1)
#     else:
#         return binary_search(ary, target, mid+1, end)





# print(binary_search(array, 0, 0, max_value))





### 다른 사람 풀이
N,M = map(int,input().split())
lecs = list(map(int,input().split()))

lo = max(lecs)
hi = sum(lecs)
mid = (lo+hi)//2
ans = hi

def get_cnt(m):
    temp = 0
    cnt = 0
    for lec in lecs:
        if lec <= temp:
            temp = temp-lec
        else:
            temp = m - lec
            cnt += 1

        print("get_cnt : ", lec, temp, cnt, m)
    return cnt
            
while lo<=hi:
    if get_cnt(mid)<=M:
        ans = mid
        hi = mid-1
    else:
        lo = mid+1

    print("binary_search : ", ans, lo, hi)
    mid = (lo+hi)//2
    

print(mid+1)