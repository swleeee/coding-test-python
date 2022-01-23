import sys
input = sys.stdin.readline

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))


def solution(n, lost, reserve):    
    answer = 0
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))

    print("new_lost : ", new_lost)
    print("new_reserve : ", new_reserve)
    
    answer = n - len(new_lost)

    for i in new_lost:
        if i-1 in new_reserve:
            answer += 1
            new_reserve.remove(i-1)
        elif i+1 in new_reserve:
            answer += 1
            new_reserve.remove(i+1)

    return answer

print(solution(n, lost, reserve))


# def solution(n, lost, reserve):    
#     ary = [0] * (n+1)

#     answer = n - len(lost)
#     for i in lost:
#         ary[i] += 1

#     for i in reserve:
#         ary[i] += 1

#     for i in range(1, n+1):
#         if ary[i] == 2:
#             lost.remove(i)
#             reserve.remove(i)
#             answer += 1

#     lost_flag = True
#     reserve_flag = True
#     a = 0
#     b = 0

#     lost.sort()
#     reserve.sort()
    
#     while len(lost) > 0 and len(reserve) > 0:
#         if lost_flag:
#             a = lost.pop()
#         if reserve_flag:
#             b = reserve.pop()
        
#         if abs(a - b) == 1:
#             answer += 1
#             reserve_flag = True
#             lost_flag = True
#         else:
#             if a < b:
#                 lost_flag = False
#                 reserve_flag = True
#             else:
#                 lost_flag = True
#                 reserve_flag = False

#     return answer


# TC / 3, 7




### good 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

