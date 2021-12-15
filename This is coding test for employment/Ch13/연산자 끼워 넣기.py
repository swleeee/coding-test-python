import sys
input = sys.stdin.readline
from itertools import permutations

# n = int(input())
# data = list(map(int, input().split()))
# operator_count_list = list(map(int, input().split()))



# print("data : ", data)
# print("operator_count_list : ", operator_count_list)

# operator_list = []

# for count in range(len(operator_count_list)):
#     for _ in range(operator_count_list[count]):
#         if count == 0:
#             operator_list.append('+')
#         elif count == 1:
#             operator_list.append('-')
#         elif count == 2:
#             operator_list.append('*')
#         else:
#             operator_list.append('/')


# print("operator_list", operator_list)


# opt_permu_list = list(permutations(operator_list, n-1))

# print("opt_permu_list", opt_permu_list)

# opt_permu_list = list(set(opt_permu_list))

# print(len(opt_permu_list))

# min_value = 10 ** 9
# max_value = -(10 ** 9)

# print(min, max)

# for case in opt_permu_list:
#     print("case", case)
#     expression = data[0]
#     for i in range(len(case)):
        
#         if case[i] == '+':
#             expression += data[i+1]
#         elif case[i] == '-':
#             expression -= data[i+1]
#         elif case[i] == '*':
#             expression *= data[i+1]
#         elif case[i] == '/':
#             if expression < 0:
#                 expression *= -1
#                 expression //= data[i+1]
#                 expression *= -1
#             else:
#                 expression //= data[i+1]
#         print("case | expression", case[i], expression)

    
#     print("expression", expression)
#     min_value = min(min_value, expression)
#     max_value = max(max_value, expression)
#     # break


# # case ('-', '/', '+', '+', '*')

# # print("dd", -1 %)
# print("min | max", min_value, max_value)


### 풀이

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    # 모든 연사자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    print("i | now | add | sub | mul | div : ", i, now, add, sub, mul, div)
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

### ** 재귀적 부분이 잘 이해가 안감
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / data[i])) # 나눌 때는 나머지 제거
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)



# if plus:
#         dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
#     if minus:
#         dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
#     if multiply:
#         dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
#     if divide:
#         dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)
