
## 1) 정답
# import heapq

# def solution(genres, plays):
#     answer = []
#     dic = {}
#     for i in range(len(genres)):
#         if genres[i] in dic:
#             heapq.heappush(dic[genres[i]]["genre"], (plays[i], i))
#             dic[genres[i]]["total_count"] += plays[i]
#         else:
#             dic[genres[i]] = {}
#             dic[genres[i]]["genre"] = []
#             heapq.heappush(dic[genres[i]]["genre"], (plays[i], i))
#             # dic[genres[i]]["genre"].append(plays[i])
#             dic[genres[i]]["total_count"] = plays[i]

#     print("b : ", list(dic.items()))
#     # print("ddddd : ", list(list(dic.items())["g"]))
    
#     sorted_dic = sorted(list(dic.items()), key = lambda x : (-x[1]["total_count"], x[1]["genre"]))
    

#     print("dic : ", dic)
#     print("dic : ", sorted_dic)
#     for d in sorted_dic:
#         print("d : ", d[1]["genre"])
#         ary = sorted(list(d[1]["genre"]), key = lambda x : (-x[0], x[1]))
#         print("ary : ", ary)
#         for i in range(len(d[1]["genre"])):
#             print("i : ", d[1]["genre"][i-1], i)
#             if i > 1:
#                 break
#             else:
#                 answer.append(ary[i][1])
#     return answer

## 2) 다른 사람 풀이 1 
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    
    for e in zip(genres, plays, range(len(plays))):
        print("e : ", e)
        d[e[0]].append([e[1] , e[2]])
    print("d : ", d, list(d.keys()))
    # x는 list(d.keys())의 원소를 의미하고, map 함수 안에 있는 lambda의 y는 d[x]의 원소를 의미합니다. 따라서 x(genre)를 받아서 d[x] (dictionary d의 해당 장르에 속한 음악 고유번호와 play된 수 list)에서 play된 수만 추출하고, 그 값들을 모두 합한 값을 key로 sorted
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True) 
    print("genreSort : ", genreSort)
    print()
    for g in genreSort:
        print("g : ", g)
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        print("temp : ", temp)
        answer += temp[:min(len(temp),2)]
    return answer

# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]
## 4, 1, 3, 0

genres = ["classic", "pop", "classic", "classic","jazz","pop", "Rock", "jazz"]
plays = [500, 600, 150, 800, 1100, 2500, 100, 1000]
## 5, 1, 4, 7, 3, 0, 6

# genres = ["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"]
# plays = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
## 0, 1, 2, 4


print(solution(genres, plays))