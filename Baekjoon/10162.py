time_type = [300, 60, 10]
count_ary = [0, 0, 0]

n = int(input())

for i in range(len(time_type)):
    if(n>=time_type[i]):
        count_ary[i] += (n // time_type[i])
        n %= time_type[i]

if(n==0):
    for s in count_ary:
        print(s, end=" ")
else:
    print(-1)