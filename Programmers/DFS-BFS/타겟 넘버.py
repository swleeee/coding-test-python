import sys
sys.setrecursionlimit(10 ** 5)

### 1) 정답
# operator = ['-', '+']
# def dfs(numbers, result, count, length, target, answer):
#     print("bbb : ", count, result)
#     if count > 0:
        
        
#         # for op in operator:
#             # if op == "-":
#                 # result -= numbers[length-count]
#                 # print("op : ", op)
#         print(result - numbers[length-count])
#         dfs(numbers, result - numbers[length-count], count-1, length, target, answer)
#             # else: 
#                 # result += numbers[length-count]
#         dfs(numbers, result + numbers[length-count], count-1, length, target, answer)
        
    
#     else:
#         if result == target:
#             answer[0] += 1
#         print("answer~ : ", answer, result)
        


# def solution(numbers, target):
#     answer = [0]
#     length = len(numbers)
#     dfs(numbers, 0, length, length, target, answer)
#     print(answer[0])
#     return answer[0]

### 2) 다른 사람 풀이 1 (재귀 - 이해가 잘 안 감..)
# def solution(numbers, target):
#     print("numbers | target : ", numbers, target)
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

### 3) 다른 사람 풀이 2 (product)
# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     # print("product : ", list(product(l, repeat=2)))
#     print("product : ", list(product(*l)))
#     s = list(map(sum, product(*l)))
#     print("l : ", l)
#     print("s : ", s)
#     return s.count(target)

### 4) 다른 사람 풀이 3
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer


# numbers = [1, 1, 1, 1, 1]
# target = 3

numbers = [1, 2, 3, 4, 5]
target = 6
print(solution(numbers, target))

# print(int(operator[0]) + 3)