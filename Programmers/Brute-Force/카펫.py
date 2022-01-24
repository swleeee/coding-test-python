### 1) 정답 (둘레 이용)
def solution(brown, yellow):
    answer = []    
    # print("yellow 제곱근 : ", int(yellow ** (1/2)))
    grid = 0
    for i in range(1, int(yellow ** (1/2))+1):
        # print("i : ", i)
        if yellow % i == 0:
            grid = i*2 + (yellow // i + 2) * 2
            if grid == brown:
                answer.append(yellow // i + 2)
                answer.append(i + 2)

    return answer


# brown = 12
# yellow = 4
## [4, 4]

# brown = 10
# yellow = 2
## [4, 3]

# brown = 8
# yellow = 1
# # [3, 3]

# brown = 24
# yellow = 24
# # [8, 6]

print(solution(brown, yellow))