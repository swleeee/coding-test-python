import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a.sort(reverse=True)

standard_idx = a[0]

a.sort()

sort_ary = []
for i in range(n):
    sort_ary.append([standard_idx + b[i], i])

sort_ary.sort(key=lambda x: -x[0])



print(sort_ary)

count = 0

for i in range(n):
    print("a", a[i])
    print("b", sort_ary[i][0]-standard_idx)
    count += a[i] * (sort_ary[i][0]-standard_idx)

print(count)



## 정답
# A배열의 최소 * B배열의 최대 연산 후 pop으로 요소
