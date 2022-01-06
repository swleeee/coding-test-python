import sys
input = sys.stdin.readline

array = [0] * 90
array[0] = 1
array[1] = 1

n = int(input())

if n > 2:
    for i in range(3, n+1):
        array[i-1] = array[i-2] + array[i-3]

print(array[n-1])
# print(array)