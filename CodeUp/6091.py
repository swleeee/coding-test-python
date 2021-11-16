# 6091 : [기초-종합] 함께 문제 푸는 날(설명)

n, m, o = map(int, input().split())
d = 1
while d%n!=0 or d%m !=0 or d%o !=0 :
    d+=1
print(d)