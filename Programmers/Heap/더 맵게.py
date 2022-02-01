import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
            # break
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        s3 = s1 + s2 * 2
        heapq.heappush(scoville, s3)
        answer += 1        
    print("scoville : ", scoville)
    # if len(scoville) == 0:
    #     return -1
    # else:
    return answer
    # return answer

# scoville = [1, 2, 3, 9, 10, 12]
scoville = [1, 2, 3, 4]
K = 28
print(solution(scoville, K))