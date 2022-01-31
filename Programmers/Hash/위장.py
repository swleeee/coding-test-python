## 1) 정답
# def solution(clothes):
#     answer = 1
#     dic = {}
#     for cloth in clothes:
#         if cloth[1] in dic:
#             count = dic.get(cloth[1])
#             dic[cloth[1]] = count + 1
#         else:
#             dic[cloth[1]] = 1
#     # print("dic : ", dic.values())
    
#     for d in dic.values():
#         answer *= (d+1)
    

#     return answer-1

## 2) 다른 사람 풀이 1 (해시)
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))