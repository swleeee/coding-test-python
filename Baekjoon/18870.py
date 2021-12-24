# import sys
# input = sys.stdin.readline

# n = int(input())
# data = list(map(int, input().split()))

# loc = []

# for i in range(len(data)):
#     loc.append((i, data[i]))


# loc.sort(key=lambda x : x[1])

# idx = 0
# value = loc[0][1]
# result = []

# for s in loc: 
#     if value != s[1]:
#         idx += 1    
        
#     result.append((s[0], idx))
#     value = s[1]

# result.sort(key=lambda x : x[0])
# for s in result:
#     print(s[1], end=' ')




### 풀이

n = int(input())
data = list(map(int, input().split()))
rank_dic = dict()
answer = []
s_data = sorted(set(data))
print("s_data : ", s_data)
for idx, i in enumerate(s_data):
    rank_dic[i] = idx
    print("idx | i | rank_dic : ", idx, i, rank_dic)

for d in data:
    answer.append(str(rank_dic[d]))
    print("d | answer : ", d, answer)
print(' '.join(answer))