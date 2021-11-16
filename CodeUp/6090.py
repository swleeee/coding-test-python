# 6090 : [기초-종합] 수 나열하기3

n, m, o, p = map(int, input().split())
total = n

for i in range(1, p):
    total = total * m + o    
print(total)