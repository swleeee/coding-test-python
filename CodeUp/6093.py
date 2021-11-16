# 6093 : [기초-리스트] 이상한 출석 번호 부르기2

n = int(input())
s = input().split()

for i in range(1, n+1):
    print(s[n-i], end=" ")

# for i in range(n-1, -1, -1) :
#   print(s[i], end=' ')