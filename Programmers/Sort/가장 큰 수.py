### 1) 정답
# def solution(numbers):
#     answer = ''
#     data = []
#     for i, number in enumerate(numbers):
#         number = str(number)
#         length = len(number)

#         if length == 4:
#             data.append((int(number), 4, i))
#         elif length == 3:
#             data.append((int(number+number[0]), 3, i))
#         elif length == 2:
#             data.append((int(number*2), 2, i))
#         else:
#             data.append((int(number*4), 1, i))

#     data.sort(key=lambda x: (-x[0], x[1]))

#     for s in data:
#         answer += str(numbers[s[2]])
#     # print(type(answer))
#     answer = str(int(answer))
#     return answer


# numbers = [6, 10, 2]
# numbers = [3, 30, 34, 5, 9]
# numbers = [30, 302]
# numbers = [10, 101]
# numbers = [1, 11, 111, 1111]
# numbers = [0, 0, 0, 0, 0, 0]
# numbers = [0, 0, 70]
numbers = [2, 20, 200]

### 2) 다른 사람 풀이 
def solution(numbers):
    answer = ''
    numbers = sorted(numbers, reverse=True, key=lambda  x: (str(x)*4).ljust(4))
    for i in numbers:
        answer += str(i)
    if answer[0] == '0':    #모두 0인 경우 -> 테스트11
        return '0'
    return answer

print(solution(numbers))