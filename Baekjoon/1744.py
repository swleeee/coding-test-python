import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
minus = []
zero = []
# one = []
plus = []
count = 0
for i in range(n):
    a = int(input())
    if a <= 0:
        minus.append(a)
    # elif a == 0:
        # zero.append(a)
    elif a == 1:
        count += 1
    else:
        plus.append(a)

plus.sort()
minus.sort(reverse=True)

# print("minus : ", minus)
# print("plus : ", plus)

def bind_value(ary):
    global count 
    while len(ary) > 0:
        if len(ary) > 1:
            a = ary.pop()
            b = ary.pop()
            count += a*b

        if len(ary) == 1:
            a = ary.pop()
            # print("a : ", a)
            # print(type(a))
            # print(type(count))
            count += a
        # print("ary : ", ary)

bind_value(minus)
bind_value(plus)
print(count)