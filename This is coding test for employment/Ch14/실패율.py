n = int(input())
stages = list(map(int, input().split()))

# stages.sort()
print("stages : ", stages)


# challenge_person = 0

# ary = []

# def solution(stages):
#     person = len(stages)
#     stage=1

#     count = 0
#     # for i in range(n):
#     for i in range(len(stages)):
#         if stages[i] > n:
#             if stage < n:                
#                 for j in range(stage+1, n+1):
#                     ary.append((j, 0))
#         else:
#             if stage == stages[i]:
#                 count += 1
#             else:
#                 ary.append((stage, count / person))
#                 person -= count
#                 count = 1
#                 stage += 1

# solution(stages)

# print(ary)




### 풀이

def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)

        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length

        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer


print(solution(n, stages))


## Input Data
# 5
# 2 1 2 6 2 4 3 3

# 1 2 2 2 3 3 4 6  