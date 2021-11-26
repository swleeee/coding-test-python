n, m = map(int, input().split())

count = 0

while True:
    if(m==n):
        count += 1
        break
    elif(m>n):        
        # 일의자리가 1이면 1을 오른쪽에 추가한 경우임
        if(m % 10 == 1):
            m //= 10
            count += 1
            continue

        # 홀수는 만들 수 없으므로 -1
        elif(m % 2 == 1):
            count = -1
            break

        # 그 외에는 2를 곱한 경우임
        else:
            m //= 2
            count += 1
            continue
    else:
        count = -1
        break

print(count)