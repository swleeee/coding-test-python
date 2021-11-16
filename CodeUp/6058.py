# 6058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기

n, m = map(int, input().split())
n = bool(n)
m = bool(m)

# print((not n) and (not m)) 
print(not(n or m))
