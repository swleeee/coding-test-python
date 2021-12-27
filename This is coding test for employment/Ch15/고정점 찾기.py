import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

def binary_search(ary, start, end):
    if start > end:        
        return None
    
    mid = (start+end)//2

    if mid == ary[mid]:
        return mid
    elif mid < ary[mid]:
        return binary_search(ary, start, mid-1)
    else:
        return binary_search(ary, mid+1, end)

    

result = binary_search(data, 0, n-1)


if result == None:
    print(-1)
else:
    print(result)


### Input Data
# 5
# -15 -6 1 3 7

# 7
# -15 -4 2 8 9 13 15

# 7
# -15 -4 3 8 9 13 15