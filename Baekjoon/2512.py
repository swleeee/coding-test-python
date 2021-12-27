import sys
input = sys.stdin.readline

n = int(input())
budget_ary = list(map(int, input().split()))
total_budget = int(input())

# budget_ary.sort()
start = 0
end = max(budget_ary)
result = 0

while start <= end:
    mid = (start+end)//2

    count = 0
    
    for budget in budget_ary:
        if budget < mid:
            count += budget
        else:
            count += mid

    if total_budget >= count:
        start=mid+1
        result = mid
    else:        
        end=mid-1
        result = end
    # print("aaa : ", result, mid, start, end, count)

# print("result : ", result)
print(result)


# binary_search(ary, target, start, end):

# binary_