# 6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)

n = int(input())

if(n < 0):
    if(n % 2 == 0):
        print("A")
    elif(n % 2 == 1):
        print("B")
else:
    if(n % 2 == 0):
        print("C")
    elif(n % 2 == 1):
        print("D")