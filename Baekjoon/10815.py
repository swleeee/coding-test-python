import sys
input = sys.stdin.readline

n = int(input())
card = set(list(map(int, input().split())))


m = int(input())
data = list(map(int, input().split()))

# answer = []

for num in data:
    if num in card:
        # answer.append(1)
        print(1, end=' ')
    else:
        # answer.append(0)
        print(0, end=' ')

# for ans in answer:
#     print(ans, end=' ')