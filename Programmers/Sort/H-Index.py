

### 1)
# from bisect import bisect_left

# def solution(citations):
#     answer = 0
#     citations.sort()
#     length = len(citations)
#     # print("citiations | length : ", citiations, length)
#     def count_index(citations, start, x, end, length):

#         idx = bisect_left(citations, x)
#         print("start | x | end | idx : ", start, x, end, idx)
#         if start == end:
#             if x <= length - idx  and x >= idx:
#                 print("a")
#                 return x
#             else:
#                 print("b")
#                 return x-1
#         else:
#             if x <= length - idx and x >= idx:
#                 print("c")
#                 return count_index(citations, x, (end+x)//2, end, length)
#             else:
#                 print("d")
#                 # if x <= length - idx - 1:
#                 return count_index(citations, start, (start+x)//2, x, length)




#     print("aaa : ", count_index(citations, 0, citations[-1] // 2, citations[-1], length))

#     # print(bisect_left(citations, length))
#     return answer

### 2) 정답
# from bisect import bisect_left

# def solution(citations):
#     answer = 0
#     citations.sort()
#     length = len(citations)
#     # print("citiations | length : ", citiations, length)

#     start = 0
#     end = citations[-1]
#     answer = 0

#     while(start <= end):
#         total = 0
#         mid = (start + end) // 2
      
#         idx = bisect_left(citations, mid)

        
#         if mid <= length - idx and mid >= idx:
#             start = mid + 1
#             answer = mid
#         else:
#             end = mid - 1
    
#     # print("answer : ", answer)

#     # print(bisect_left(citations, length))
#     return answer

### 3) 다른 사람 풀이 1 (코드는 이해했는데 왜 정답이 될 수 있는지 잘 이해가 안 감.. 지금 이해ok)
# def solution(citations):
#     citations.sort(reverse=True)
#     print("citations : ", citations)
#     print("aaa : ", list(map(min, enumerate(citations, start=1))))
#     answer = max(map(min, enumerate(citations, start=1))) # (해당 인용수 이상의 논문개수와 해당 논문의 인용수) 중 더 작은 숫자
#     return answer

### 4) 다른 사람 풀이 2
def solution(citations):
    citations = sorted(citations)
    print("citations : ", citations)
    l = len(citations)
    for i in range(l):
        print("l | i | l-i : ", l, i, l-i)
        if citations[i] >= l-i:
            return l-i
    return 0

citations = [3, 0, 6, 1, 5]
# citations = [0, 2, 5, 10, 14, 21]
print(solution(citations))

