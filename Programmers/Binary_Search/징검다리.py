def solution(distance, rocks, n):
    answer = 0
    start = 1
    end = distance
    rocks.append(distance)
    rocks.sort()
    

    while start <= end:
        mid = (start + end) // 2
        count = 0
        prev_rock = 0
        for rock in rocks:
            if rock - prev_rock >= mid:
                prev_rock = rock
            else:
                count += 1

        if count > n:
            end = mid-1

        else:
            start = mid + 1
            answer = mid
        


    return answer

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2

print(solution(distance, rocks, n))