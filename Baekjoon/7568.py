import sys
input = sys.stdin.readline

n = int(input())
data = []
answer = [1 for _ in range(n)]

for i in range(n):    
    data.append(list(map(int, input().split())))
    data[i].append(i)


data = sorted(data, key=lambda x:x[0])

for i in range(n):
    count = 0
    for j in range(n):
        if(data[i][1] < data[j][1] and i < j and data[i][0] < data[j][0]):
            count += 1

    answer[data[i][2]] += count

# print(answer)

# print(data)
# print(answer)

for s in answer:
    print(s, end=" ")

