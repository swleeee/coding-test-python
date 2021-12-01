import sys
input = sys.stdin.readline

n = int(input())
maps = [[0] * (n+1) for _ in range(n+1)]

# print(maps)
build_frame=[[0,0,0,1], [2,0,0,1], [4,0,0,1], [0,1,1,1], [1,1,1,1], [2,1,1,1], [3,1,1,1], [2,0,0,0], [1,1,1,0], [2,2,0,1]]
build_length = len(build_frame)

# for build_piece in build_frame:
#     # print(build_piece)
#     x, y, material, action = map(int, build_piece)
#     print(x, y, material, action)

#     # 기둥
#     if(material == 0):
#         # 설치
#         if(action == 1):
#             if y==0:
#                 maps[n-y][x] = 2
#                 maps[n-y-1][x] = 2
#         # 삭제
#         else:
#             pass

#     # 보
#     else:
#         # 설치
#         if(action == 1):
#             if(x != n):
#                 if(maps[n-y][x] == 2):
#                     maps[n-y][x+1] = 1
#                 elif(maps[n-y][x+1] == 2):
#                     maps[n-y][x] = 1
#                 elif(maps[n-y][x] == 1 and maps[n-y][x+1] == 1):
#                     pass
#                 else:
#                     pass
#             else:
#                 pass            
#         # 삭제
#         else:
#             pass

# print(maps)

# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1,0] in answer:
                continue
            return False # 아니라면 거짓 반환
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False # 아니라면 거짓 반환

    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame: # 작업(frame)의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate ==0 : # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                
                answer.append([x, y, stuff]) # 가능한 구조물이 아니라면 다시 설치
        if operate == 1: # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니라면 다시 제거

    return sorted(answer) # 정렬된 결과를 반환

print(solution(n, build_frame))
