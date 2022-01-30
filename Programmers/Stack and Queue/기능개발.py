def solution(progresses, speeds):
    answer = []
    times = []
    for i, progress in enumerate(progresses):
        # print((100-progress-1) // speeds[i] + 1)
        times.append((100-progress-1) // speeds[i] + 1)
    print("times : ", times)
    value = times[0]
    count = 1
    for i in range(len(times)-1):
        print("value : ", value)
        if value < times[i+1]:
            # count += 1
            print("a")
            value = times[i+1]
            answer.append(count)
            count = 1
        else:
            count += 1
    
    # if count != 1:
    #     print
    answer.append(count)


    return answer

# progresses = [93, 30, 55]	
# speeds = 	[1, 30, 5]

progresses = [95, 90, 99, 99, 80, 99]	
speeds = 	[1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))