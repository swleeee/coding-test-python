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
max = 0

for i in range(n):
    ary = list(map(int, input().split()))
    ary.sort()
    if(max < ary[0]):
        max = ary[0]


# print(ary)
print(max)


## 풀이

# n, m = map(int, (input().split()))
# result = 0

# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)
        
# print(result)



end_time = time.time()
print(end_time)
print("time :", end_time - start_time)
memory_usage("END") 