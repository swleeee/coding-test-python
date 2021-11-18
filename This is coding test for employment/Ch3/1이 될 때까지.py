import time 
import psutil
start_time = time.time()
print(start_time)

def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")


## 
n, m = map(int, (input().split()))
count = 0

while 1:
    # 더 이상 나눌 수 없을 때까지 나누기
    if(n>=m):
        count += n % m + 1        
        n = n//m

    # 더 이상 나눌 수 없기 때문에 1이 될 때까지 빼서 count 계산
    else:
        count += (n-1)
        break
print(count)



## 풀이
# n, k = map(int, (input().split()))
# result = 0

# while True:
#     # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
#     target = (n // k) * k
#     result += (n - target)
#     n = target
#     # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break
#     # K로 나누기
#     result += 1
#     n //= k

# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n-1)
# print(result)



end_time = time.time()
print(end_time)  
print("time :", end_time - start_time)
memory_usage("END") 