
## 1) 정답
# from collections import deque

# def solution(jobs):
#     answer = 0
#     # jobs = deque(jobs)
#     # heapq.heapify(jobs)
#     length = len(jobs)
#     jobs = sorted(jobs, key=lambda x:(x[0], x[1]))
#     print("jobs : ", jobs)
#     time = jobs[0][0]
#     # current_jobs = [job for job in jobs if job[0] <= time]
#     current_jobs = []
    
#     while jobs or current_jobs:
#         # current_jobs = [job for job in jobs if job[0] <= time]
#         print("ee : ", jobs)
#         count = 0
#         for job in jobs:
#             if job[0] <= time:
#                 count += 1
#                 current_jobs.append((job[0], job[1]))
        
#         if (len(jobs) > 0) and (len(current_jobs) == 0):
            
#             count += 1
#             current_jobs.append((jobs[0][0], jobs[0][1]))
#             task = current_jobs.pop()
#             time = task[0]
#             print("ff : ", task, time)
#             time += task[1]
#             if count:
#                 jobs = jobs[count:]
#             # task = current_jobs.pop(0)
#             answer += time-task[0]
#             print("ff : ", task, time)
#         else:

#             print("cc : ", current_jobs)
#             current_jobs = sorted(current_jobs, key=lambda x : x[1])
            
#             if count:
#                 jobs = jobs[count:]
#             print("aa : ", jobs)
#             print("current_jobs : ", current_jobs)
#             task = current_jobs.pop(0)
#             print("task : ", task)
#             time += task[1]
#             print("time : ", time)
#             answer += time-task[0]
            
#         print("answer : ", answer)
#         print()
#     return answer // length


## 2) 다른 사람 풀이 1
import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    print("tasks : ", tasks)
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)


jobs = [[1, 9], [0, 3], [30, 3], [2, 6]] 
## 7

# jobs = [[0, 3], [1, 9], [2, 6]]

print(solution(jobs))