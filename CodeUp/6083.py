# 6083 : [기초-종합] 빛 섞어 색 만들기(설명)

n, m, o = map(int, input().split())
count = 0

for i in range(n):
    for j in range(m):
        for k in range(o):
            print(i, j, k)
            count += 1

print(count)

