n, m, k = map(int, input().split())

count = 0

# 인턴 인원을 제외하고 대회에 나갈 수 있는 최대 인원 계산
min_count = (n+m-k)//3

# (여학생 2명, 남학생 1명)을 팀으로 결성할 수 있는 최대 개수 계산
if(2*m <= n):
    count += m    
else:
    # print("n", n)    
    count += n // 2

print(min(count,min_count))
