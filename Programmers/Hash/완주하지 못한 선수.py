## 1) 정답
# def solution(participant, completion):
#     answer = ''
#     dict = {}
#     for person in participant:
#         if person in dict:
#             count = dict.get(person)
#             dict[person] = count + 1
#             # print(dict.get(person))
#         else:
#             dict[person] = 1

#     print("dict : ", dict)

#     for person in completion:
#         if person in dict:
#             count = dict.get(person)
#             if count > 1:
#                 dict[person] = count -1 
#             else:
#                 del dict[person]
#             # print(dict.get(person))
#         # else:
#         #     dict[person] = 1

#     print("dict : ", dict)
#     # answer = dict.keys()
#     for k in dict.keys():
#         answer = k

#     return answer

## 2) 다른 사람 풀이 1 (Counter)
# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     print("Answer : ", answer)
#     return list(answer.keys())[0]

## 3) 다른 사람 풀이 2 (해시)
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
        print("dic | temp : ", dic, temp)
    print()
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))