
## 0 (정답)
# from collections import deque
# def solution(priorities, location):
#     answer = 0
#     docs = deque()
#     for i, priority in enumerate(priorities):
#         docs.append((priority, i))

#     print("docs : ", docs)
#     print(max(docs)[0])
#     result = []
#     while docs:
#     # for i in range(0, 10):
#         print("docs : ", docs)
#         max_value = max(docs)[0]
#         doc = docs.popleft()
#         print()
#         print("doc : ", doc[0], max_value)
#         if doc[0] == max_value:
#             result.append(doc)
#         else:
#             docs.append(doc)

#     print("result : ", result)

#     for i, doc in enumerate(result):
#         # print("aaa : ", doc)
#         if doc[1] == location:
#             answer = i+1
#             break

#     return answer

## 1) 다른 사람 풀이 1 (any)
# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
    
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#             print("queue : ", queue)
#         else:
#             answer += 1
#             print("aaa : ", cur, answer)
#             if cur[0] == location:
#                 return answer
#         print()

## 2) 다른 사람 풀이 2

def solution(priorities, location):
    answer = 0
    search, c = sorted(priorities, reverse=True), 0
    print("aaa : ", priorities, search, c)
    while True:
        for i, priority in enumerate(priorities):            
            s = search[c]
            print("bbb : ", i, priority, search, c, s)
            if priority == s:
                c += 1
                answer += 1
                if i == location:
                    break
        else:
            continue
        break
    return answer


# priorities = [2, 1, 3, 2]
# location = 2
## 1

priorities = [1, 1, 9, 1, 1, 1]
location = 0
## 5
print(solution(priorities, location))