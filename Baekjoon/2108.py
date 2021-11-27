# import sys
# input = sys.stdin.readline

# n = int(input())
# ary = []
# for _ in range(n):
#     ary.append(int(input()))

# ary.sort()

# count = 1
# max_value = 1
# new_num = ary[0]
# # fre_ary = [ary[0]]
# fre_ary=[]

# for i in range(1, len(ary)):
#     print(i, max_value, count, fre_ary)
#     if new_num == ary[i]:
#         count += 1
#     else:
        
#         if max_value < count:
#             fre_ary.clear()
#             fre_ary.append(new_num)
#             max_value = count
#             count = 1
#         elif max_value == count:
#             fre_ary.append(new_num)
#             count = 1
#         else:
#             count = 1
        
#         new_num = ary[i]

# fre_ary.sort()

# if max_value < count:
#     fre_ary.clear()
#     fre_ary.append(new_num)
#     max_value = count
#     count = 1
# elif max_value == count:
#     fre_ary.append(new_num)
#     count = 1
# else:
#     count = 1

# print("ary", ary)
# print("fre_ary", fre_ary)

# print(round(sum(ary)/len(ary)))
    
# # print(ary[n//2])
# print(ary[int((len(ary)-1)/2)])
# if(len(fre_ary) == 1):
#     print(fre_ary[0])
# else:
#     print(fre_ary[1])
# print(max(ary)-min(ary))



### 괜찮은 풀이

import sys
from collections import Counter

N = int(sys.stdin.readline())
A = sorted([int(sys.stdin.readline()) for _ in range(N)])


def Avg():
    return round(sum(A) / N)


def Mid():
    return A[N // 2]


def Mode():
    mode = Counter(A).most_common(2)
    print("mode", mode)
    if len(mode) > 1 and mode[0][1] == mode[1][1]:
        return mode[1][0]
    else:
        return mode[0][0]


def Range():
    return max(A) - min(A)


print(Avg())
print(Mid())
print(Mode())
print(Range())