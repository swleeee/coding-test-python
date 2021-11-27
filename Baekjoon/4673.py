import time 
import psutil
start_time = time.time()


def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")


# ary= set()

# def cal(n):
#     global ary
#     new_num = n + sum(list(map(int, str(n))))
#     if(new_num <= 10000):
#         if(new_num not in list(ary)):
#             ary.add(new_num)
#             cal(new_num)        
            
#     # print(new_num)


# for i in range(1, 10001):
#     if(i not in list(ary)):
#         print(i, sep=" ")
#         cal(i)
#     else:
#         continue
        

# cal(101)
# cal(100)
# ary.sort()
# ary = list(ary)
# ary.sort()
# print(ary)
# print(''.join(ary))



### 풀이1

def d(s):
    print("s :", s)
    result = sum(int(i) for i in str(s))
    result += s
    print("result :", result)
    return result

total_list = [d(i) for i in range(1,15)]
print("total_list", set(total_list))
list_10000 = [x for x in range(1,15)]
for i in sorted(set(list_10000)-set(total_list)):
    print(i)


end_time = time.time()
print(end_time)  
print("time :", end_time - start_time)
memory_usage("END") 



