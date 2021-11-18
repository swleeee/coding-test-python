import time 
import psutil
start_time = time.time()

def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")


## 
n, m, k = map(int, input().split())
ary = list(map(int, input().split()))
ary.sort()
count = 0
quotient = 0
remainder = 0

one = ary[n-1]
two = ary[n-2]
# print(one)
# print(two)
if(one==two):
    count = one * m
else:
    quotient = m // (k+1)
    remainder = m % (k+1)
    # print(quotient)
    # print(remainder)
    count = (quotient * k *one) + (quotient * two) + (remainder * one)

print(count)

print("=========================")

## 풀이1
# '가장 큰 수를 k번 더하고 두 번째로 큰 수를 한 번 더하는 연산' 반복

# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()
# first = data[n-1]
# second = data[n-2]

# result = 0

# while True:
#     for i in range(k):
#         if m==0:
#             break
#         result += first
#         m -= 1
#     if m== 0:
#         break
#     result += second
#     m-=1

# print(result)

## 풀이2

# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()
# first = data[n-1]
# second = data[n-2]

# # 가장 큰 수가 더해지는 횟수 계산
# count = int(m / (k+1)) * k
# count += m % (k+1)

# result = 0
# result += (count) * first # 가장 큰 수 더하기
# result += (m-count) * second # 두 번째로 큰 수 더하기

# print(result)

end_time = time.time()
print("time :", end_time - start_time)
memory_usage("END") 