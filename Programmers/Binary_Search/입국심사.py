def solution(n, times):
    answer = 0
    times.sort()
    start = 0
    end = times[-1] * n

    while start <= end:
        mid = (start+end) // 2
        # print("mid : ", mid)

        result = 0
        for time in times:
            result += (mid//time)
        
        if result >= n:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1

    return answer



# n = 6
# times = [7, 10]
## 6 

# n = 8
# times = [5, 7, 10, 12]
## 22

n = 8
times = [5, 7, 12]

print(solution(n, times))