def solution(N, number):
    answer = 0
    dp = []
    
    for i in range(1, 9):
        cases = set()
        cases.add(int((str(N) * i)))

        for j in range(0, i-1):
            for op1 in dp[j]:
                for op2 in dp[i-j-2]:
                    cases.add(op1 + op2)
                    cases.add(op1 - op2)
                    cases.add(op1 * op2)
                    if op2 != 0:
                        cases.add(op1 // op2)

        for case in cases:
            if case == number:
                answer = i
                break

        if case == number:
            break

 
        dp.append(cases)


    print(cases, dp)
    if answer == 0:
        answer = -1


    return answer

# N = 5
# number = 12
## 4

N = 5
number = 31168

print(solution(N, number))