# 6092 : [기초-리스트] 이상한 출석 번호 부르기1(설명)

n = int(input())
s = input().split()
list = []

for i in range(23):
    list.append(0)

for i in range(1, n+1):
    list[int(s[i-1])-1] += 1

for i in list:
    print(i, end=" ")