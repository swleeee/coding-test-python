import time 
import psutil
start_time = time.time()

def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")


## 
n = int(input())
list = [500, 100, 50, 10]
count = 0

for i in range(len(list)):   
    count += n//list[i]
    n = n%list[i]
    
print(count)

## 풀이
# n = int(input())
# count = 0

# coin_types = [500, 100, 50, 10]

# for coin in coin_types:   
#     count += n // coin
#     n %= coin
    
# print(count)


end_time = time.time()
print("time :", end_time - start_time)
memory_usage("END") 