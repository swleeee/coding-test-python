n = int(input())
origin_data = n

# print(len(str(n)))
count = 0
while True:

    ## 한 자릿수인 경우 
    if(len(str(n)) == 1):
        n = int(str(n) + str(n))

    ## 두 자릿수인 경우
    else:
        data = str(n)
    # total = str(int(data[0]) + int(data[1]))
    # new_data = str[1]
        total = sum(list(map(int, str(n))))
        if(total >= 10):
            total %= 10
        n = int(data[1] + str(total))

    count += 1
    if(origin_data == n):        
        break

    # print(count, n)
# print(data)
# print(total)
# print(n)
print(count)
# print(new_data)

# if(n < 10):
#     n = int('0' + str(n))
# print(n)






### 괜찮은 풀이
N = int(input())
num = N
cnt = 0
while True:
  fir = num%10*10
  sec = (num//10+num%10)%10
  num = fir + sec
  cnt += 1
  if N == num:
    break
print(cnt)