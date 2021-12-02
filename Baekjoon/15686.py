from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
home_list = []
chicken_list = []
# d = []
# for i in range(N):
#     d.clear()
#     d = list(map(int, input().split()))
#     print("d", d)
    

# print(maps)

# home_list = [(i, j) for i in range(N) for j in range(N) if maps[i][j] == 1]
for i in range(N):
    for j in range(N):
        if(maps[i][j] == 1):
            home_list.append((i,j))
        if(maps[i][j] == 2):
            chicken_list.append((i,j))

# print(home_list)
# print(chicken_list)

result = list(combinations(chicken_list, M))
# print("result", result)


min_distance = 10000
min_value = 10000
total_value = 0
value = 0

def calc(case):
    global home_list
    global total_value
    global min_value
    global min_distance
    value = 0
    for i in range(len(home_list)):
        # print("num", home_list[i], case)
        # total_value = 0
        min_value = 10000
        for sub_case in case:
            # home_list[i][0] - case[]
            value = 0
            # print("sub", sub_case)            
            value += abs(sub_case[0] - home_list[i][0])
            value += abs(sub_case[1] - home_list[i][1])
            min_value = min(min_value, value)
        total_value += min_value
        # print("total_value", total_value)
    min_distance = min(min_distance, total_value)
    total_value = 0
    # print("min_distance", min_distance)


for case in result:    
    calc(case)

print(min_distance)



