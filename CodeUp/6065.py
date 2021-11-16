# 6065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)

n, m, k = map(int, input().split())

if(n % 2 == 0):
    print(n)
if(m % 2 == 0):
    print(m)
if(k % 2 == 0):
    print(k)