# 6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기(설명)

n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)

print(n+m+k, format((n+m+k)/3, ".2f"))