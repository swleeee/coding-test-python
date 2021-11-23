import sys
input = sys.stdin.readline

t = int(input())
ary = t * [0]
count_ary = t*[0]
# print(ary)

for i in range(t):
    n = int(input())
    ary[i] = n* [0]
    for j in range(n):
        input_ary = list(map(int, input().split()))
        # print(input_ary)
        ary[i][j] = input_ary
        # print(ary[i])
    ary[i].sort(key=lambda x: x[0])
    min = len(ary[i])+1                       ### 이 부분에서 반례 찾음
    count = 0
    for j in range(len(ary[i])):
        print(i, ary[i][j][1])
        if(ary[i][j][1] < min):
            print("min", min)
            count += 1
            min = ary[i][j][1]

    print("count", i, count)
    count_ary[i] = str(count)
    # print(str(count))

# print(ary)

print('\n'.join(count_ary))

    
# 이중배열로 해서 메모리를 많이 잡아 먹은듯 => 그냥 리스트로 할 수도 있을 거 같음
# 시간소요도 다른 사람들에 비해 조금 많이 나옴..