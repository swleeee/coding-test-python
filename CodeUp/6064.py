# 6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기(설명)

n, m, k = map(int, input().split())
print((n if n<m else m) if(n if n<m else m < k) else k)