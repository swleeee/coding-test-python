### 1) 정답
# def solution(array, commands):
#     answer = []
#     for start, end, index in commands:
#         # start, end, index = map(int, command)
#         print(start, end, index)
#         split_ary = array[start-1:end]
#         split_ary.sort()
#         print(split_ary, array)
#         answer.append(split_ary[index-1])
#         # array = array[:start] + split_ary + array[end+1:]
#         # print(command)

#     return answer

### 2) 다른 사람 풀이 1 - lambda or list comprehension

# def solution(array, commands):
#     # return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)) # lambda
#     return [sorted(array[a-1:b])[c-1] for a,b,c in commands] # list comprehension


### 3) 다른 사람 풀이 2
def solution(array, commands):
    answer = []
    for i, j, k in commands:        
        answer.append(sorted(array[i-1:j])[k-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))