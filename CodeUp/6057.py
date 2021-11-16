# 6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기(설명)

n, m = map(int, input().split())
n = bool(n)
m = bool(m)

print((n and m) or ((not n) and (not m))) 
