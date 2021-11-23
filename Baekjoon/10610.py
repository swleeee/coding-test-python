data = list(input())
data.sort(reverse=True)

count = 0

# 30의 배수가 되기 위한 조건 1) 맨 끝이 0이어야 함
if(data[len(data)-1] != '0'):
    print(-1)
else:
    for s in data:
        count += int(s)
    # 30의 배수가 되기 위한 조건 2) 각 자리에 있는 요소의 합이 3의 배수여야 함
    if(count % 3 ==0):
        print(''.join(data))
    else:
        print(-1)

