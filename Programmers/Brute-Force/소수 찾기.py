
### 1) 정답
# from itertools import permutations

# def solution(numbers):
#     answer = 0
#     length = len(numbers)
#     ary = [0] * length
#     for i in range(length):
#         # print(list(permutations(numbers, i+1)))
#         ary[i] = set(permutations(numbers, i+1))
#     # print("ary : ", ary)

#     # num = 0
#     data = []
#     for a in ary:
#         # print("a : ", a)
#         for b in a:
#             # print("b : ", b, b[0])
#             if b[0] != '0': 
#                 num = int(''.join(b)) # 데이터 만들기
#                 print("num : ", num)
#                 # data.append(num)
#                 if num != 1:
#                     flag = True
#                     for i in range(2, num):
#                         if num % i == 0:
#                             flag = False
#                             break
#                     if flag:
#                         data.append(num)
#     print("data : ", data)
#     answer = len(data)
#     return answer


### 2) 다른 사람 풀이 1 (set 이용)
# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#         print("a : ", a)
#     a -= set(range(0, 2))
#     print("a2 : ", a)
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#         print("a3 : ", a, set(range(i * 2, max(a) + 1, i)))
#     return len(a)

### 3) 다른 사람 풀이 2 (라이브러리 안씀.. 이해가 잘 안 감..)
primeSet = set()


def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def makeCombinations(str1, str2):
    print("str1 | str2 : ", str1, str2)
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))

    for i in range(len(str2)):
        print("make : ", str1, str2, i)
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution(numbers):
    makeCombinations("", numbers)

    answer = len(primeSet)

    return answer


numbers = "123"
# numbers = "011"
# numbers = "17"
print(solution(numbers))