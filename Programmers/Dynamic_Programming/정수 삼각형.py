def solution(triangle):
    answer = 0
    length = len(triangle)

    for i in range(1, length):
        for j in range(len(triangle[i])):
            # print(i, j, number)
            if j==0:
                triangle[i][j] += triangle[i-1][j] 
            elif i == j:
                
                triangle[i][j] += triangle[i-1][j-1] 
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    # print("ddd : ", triangle)
    answer = max(triangle[length-1])
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	
print(solution(triangle))