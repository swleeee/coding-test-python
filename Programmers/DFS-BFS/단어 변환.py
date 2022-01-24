

### 1) bfs,,
# from collections import deque
# answer = 0

# def bfs(begin, target):
#     print("begin : ", begin)
#     global answer
#     q = deque()
#     q.append(begin)
#     length = len(begin)

#     while q:
#         word = q.popleft()
#         print("word : ", word)
#         for w in words:
#             count = 0
#             for c in word:
#                 if c in w:
#                     count += 1
#             print("length | count | w | c | word | answer : ", length, count, w, c, word, answer)
#             # if count == length:
#             #     return 
#             if count == length - 1:
#                 if target == w:
#                     return
#                 else:
#                     q.append(w)
#                     # if word in words:
#                     #     words.remove(word)
#                     answer += 1

    



# def solution(begin, target, words):
#     global answer
#     if target in words:                               
#         bfs(begin, target)

#     return answer

### 2) dfs.. 실패
# import copy

# answer = 0

# def dfs(ary, begin, target, total_count=0):
#     print("begin : ", ary, begin, total_count, len(words))
#     global answer
    
#     length = len(begin)
        
#     if total_count < len(words):
#         for w in ary:
#             count = 0
#             for c in begin:
#                 if c in w:
#                     count += 1
#             print("count | w | begin | answer | total_count : ", count, w, begin, answer, total_count, ary)
#             # if count == length:
#             #     return 
#             if target == w:
#                 print("total_count : ", total_count+1)
#                 answer = min(answer, total_count+1)
#                 return 

#             if count == length - 1:
               
#                 # else:
#                 #     # print("length | count | w | c | begin | answer | total_count | ary : ", length, count, w, c, begin, answer, total_count, ary)
#                     # q.append(w)
#                 if begin in ary:
#                     ary.remove(begin)
#                 # ary.
#                 print()
#                 dfs(ary, w, target, total_count + 1)
#                 # answer += 1

        



# def solution(begin, target, words):
#     global answer
#     answer = len(words)
#     copy_words = copy.deepcopy(words)
#     if target in words:                               
#         dfs(copy_words,begin, target)

#     return answer

### 3) 정답 DFS
# answer = 0

# def dfs(words, ary, begin, target, total_count=0):
#     print("begin : ", ary, begin, total_count, len(words))
#     global answer
    
#     length = len(begin)
#     ary.append(begin)
#     if total_count < len(words):
#         for w in words:
#             count = 0
#             for i, c in enumerate(begin):
#                 if c == w[i]:
#                     count += 1
#             print("count | w | begin | answer | total_count : ", count, w, begin, answer, total_count, ary)
#             # if count == length:
#             #     return 


#             if count >= length - 1:

#                 if target == w:
#                     print("total_count : ", total_count+1)
#                     answer = min(answer, total_count+1)
#                     return 


#                 print()
#                 if w not in ary:
#                     # if begin in words:
#                     #     ary.append(w)

#                 # ary.
                
#                 # if w not in 
#                     dfs(words, ary, w, target, total_count + 1)
#                 # answer += 1
#     else:
#         answer = 0

        
# def solution(begin, target, words):
#     global answer
#     answer = len(words)
#     # copy_words = copy.deepcopy(words)
#     ary = []
#     if target in words:                               
#         dfs(words, ary, begin, target)
#     else:
#         answer = 0

#     return answer

### 4) 다른 사람 풀이 1 zip, yield

# from collections import deque

# def get_adjacent(current, words):
#     for word in words:
#         # print("words | word : ", words, word)
#         if len(current) != len(word):
#             continue

#         count = 0
#         print("zip : ", list(zip(current, word)))
#         for c, w in zip(current, word):
#             # print("c | w : ", c, w)
#             if c != w:
#                 count += 1

#         if count == 1:
#             # print("ddd : ", word)
#             yield word
#     print()


# def solution(begin, target, words):
#     dist = {begin: 0}
#     queue = deque([begin])

#     while queue:
#         print("queue : ", queue)
#         current = queue.popleft()
#         print("queue | current : ", queue, current)

#         for next_word in get_adjacent(current, words):
#             print("next_word : ", next_word)
#             if next_word not in dist:
#                 dist[next_word] = dist[current] + 1
#                 print("dist : ", dist)
#                 queue.append(next_word)

#     return dist.get(target, 0) # target이 없을 때 default 로 0

### 5) 다른 사람 풀이 2 dfs
answer = 0
def solution(begin, target, words):

    dfs(begin, target, 0, words)
    return answer

def change(fr, to):
    for i in range(len(fr)):
        if fr[:i]+fr[i+1:] == to[:i]+to[i+1:]:
            return True
    return False

def dfs(begin, target, d, words):
    global answer
    # print(begin)
    # print(words)
    if begin == target:
        # print(d)
        answer = d
        return
    else:
        if len(words) == 0:
            return 
        for w in range(len(words)):
            if change(begin, words[w]):
                word = words[:w]+words[w+1:]
                print("word : ", word, d)
                dfs(words[w], target, d+1, word)

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log"]


print(solution(begin, target, words))