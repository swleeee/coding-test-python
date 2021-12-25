import sys
input = sys.stdin.readline

n = int(input())
ary = list(map(int, input().split()))
m = int(input())
queries = [list(map(int, input().split())) for _ in range(m)]

# print("ary : ", ary)
# print("queries : ", queries)

for query in queries:
    i, j, k = query
    # print(i, j, k)
    query_ary = ary[i-1:j]
    # query_ary.sort(reverse=True)
    # print(query_ary[k-1])
    count = 0
    for s in query_ary:
        if s > k:
            count += 1

    print(count)