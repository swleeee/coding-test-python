n = int(input())
k = int(input())

sensor = list(map(int, input().split()))

sensor.sort()
# print("sensor : ", sensor)

ary = []

for i in range(1, n):
    ary.append(sensor[i]-sensor[i-1])



ary.sort(reverse=True)


if n <= k:
    print(0)
else:
    for i in range(k-1):
        ary[i] = 0
    print(sum(ary))

# print("ary : ", ary)


# 1 3 6 6 7 9



# 20 3 14 6 7 8 18 10 12 15
# 3 6 7 8 10 12 14 15 18 20


### <핵심!> n개의 센서들을 k개의 구간으로 나누는 것과 동일