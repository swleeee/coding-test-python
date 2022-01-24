### 1) 정답

# def solution(answers):
#     answer = []
#     students=["12345" * 2000, "21232425" * 1250, "3311224455" * 1000]
#     # students=["12345" * 2, "21232425" * 2, "3311224455" * 2]
#     count = [0] * 3
#     # print("students[j] : ", students[0])
#     for i, ans in enumerate(answers):
#         for j, student in enumerate(students):
#             # print("i | j | student[i] | ans : ", i, j, student[i], ans)
#             # print("type : ", type(student[i]), type(ans))
#             if int(student[i]) == ans:
#                 count[j] += 1
#     #             print("count : ", count)
#     # print("students : ", students)
#     max_value = max(count)
#     for i in range(3):
#         if count[i] == max_value:
#             answer.append(i+1)
    
#     return answer

### 2) 

def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        print("q : ", q)
        for i, v in enumerate(p):
            print("i : ", i)
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]

# answers = [1, 2, 3, 4, 5]

answers = [1, 3, 2, 4, 2]
print(solution(answers))

