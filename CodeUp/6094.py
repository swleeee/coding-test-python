# 6094 : [기초-리스트] 이상한 출석 번호 부르기3

n = int(input())
s = input().split()
min = n
# min = int(s[0])

for i in range(0, n):
    if(int(s[i]) < min):
        min = int(s[i])
    
print(min)