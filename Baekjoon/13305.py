import sys
input = sys.stdin.readline

n = int(input())
bridge = list(map(int, input().split()))
liter = list(map(int, input().split()))
count = 0
# print(bridge)
# print(liter)
min = 0

for i in range(n-1):
    ## 처음 도시에서는 무조건 다음 도시까지의 기름을 충전해야함
    if(i==0):
        min = liter[i]

    ## 도시에 도착할 때마다 다음 도시로 가기까지의 기름 요금의 최소값을 저장
    if(min > liter[i]):
        min = liter[i]

    # print(count, bridge[i], min)
    ## 이동 비용 계산
    count += bridge[i] * min

print(count)