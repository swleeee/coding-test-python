import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

def binary_search(ary, target, start, end):
    if start > end:
        return 
    
    # mid = (start + end) // 2
    liter = ary[start] + ary[end]
    
    if abs(target) > liter:
        target = liter

    if target > 0:
        return binary_search()
 
binary_search(array, 10 ** 9 + 1, 0, n-1)