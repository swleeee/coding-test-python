


# def solution(name):
#     answer = 0    
#     # print("name | ary : ", name, ary, len(name))
#     length = len(name)

#     if length == 1:
#         # answer += alphabet[]
#         answer += alphabet[ord(name[0]) - ord("A")]


#     else:        
#         a_count = 0
#         if name[1] == 'A':
#             for i in range(0, -(length), -1):
#                 answer += alphabet[ord(name[i]) - ord("A")]
#                 if name[i] == 'A':
#                     a_count += 1
#                 else:
#                     a_count = 0
            
#         else:
#             for i in range(length):
#                 answer += alphabet[ord(name[i]) - ord("A")]
#                 if name[i] == 'A':
#                     a_count += 1
#                 else:
#                     a_count = 0

#     print("a_count : ", a_count)
#     answer += length -1
#     answer -= a_count

#     return answer

### 
# def solution(name):
#     answer = 0    
#     # print("name | ary : ", name, ary, len(name))
#     length = len(name)

#     # print(name.count("A"))
#     if name.count("A") == length:
#         pass
#     else:
#         if length == 1:
#             # answer += alphabet[]
#             answer += alphabet[ord(name[0]) - ord("A")]


#         else:        
#             a_count = 0
#             not_a_list = []
#             a_idx = 0
#             count = 0
#             idx = 0

#             for i in range(length):
#                 if name[i] == 'A':
#                     a_count += 1

#                     a_idx = i
#                 else:
#                     not_a_list.append(i)
#                     # print("i : ", i)
#                     print("a_count : ", a_count, i)
#                     if a_count >= count:
#                         count = a_count
#                         idx = a_idx
#                     answer += alphabet[ord(name[i]) - ord("A")]
#                     # print("answer : ", answer)
#                     a_count = 0            

#             if a_count >= count:
#                 count = a_count
#                 idx = a_idx
#             # left_idx = idx - count
#             left_count = abs(idx - count)
#             # left_count = idx-count+1
#             right_count = length - idx - 1


#             print("a_count : ", a_count)
#             print("count : ", count)
#             print("idx : ", idx)
#             print("right_count : ", right_count)
#             print("left_count : ", left_count)

#             # if left_count + right_count > idx:
#             print("not_a_list : ", not_a_list)
           
#             if (left_count + (2*right_count) > idx and right_count + (2*left_count) > idx) and (right_count + left_count+ idx != length-1):
#                 start = not_a_list[0]
#                 end = not_a_list[-1]
#                 print("start | end : ", start, end)
#                 # for a_char in not_a_list:
#                 a = start - 0
#                 b = length-1-end
#                 print("a | b : ", a, b)
#                 if a == b:
#                     answer += length-1
#                 elif a > b:
#                     answer += length - a 
#                 else:
#                     answer += length -b -1
#                 # answer += idx+1
#             else:
#                 if left_count > right_count:
#                     answer += left_count + (2*right_count)
#                 else:
#                     answer += right_count + (2*left_count)
           
#     return answer

### 통과된 풀이
# def solution(name):
#     answer = 0    
#     length = len(name)
#     print("length : ",length)
#     if name.count("A") == length:
#         pass
#     else:
#         if length == 1:
#             # answer += alphabet[]
#             answer += alphabet[ord(name[0]) - ord("A")]


#         else:        
#             a_count = 0
#             count = 0
#             idx = 0
#             not_a_list = []
#             for i in range(length):
#                 if name[i] == 'A':
#                     a_count += 1
#                 else:
#                     # count = max(count, a_count)
#                     if count < a_count:
#                         count = a_count
#                         idx = i
#                     not_a_list.append(i)
#                     a_count = 0
#                     answer += alphabet[ord(name[i]) - ord("A")]
#                 # print("a_count : ", a_count, i)
#             if count < a_count:
#                 count = a_count
#                 idx = i

#             if idx > 0:
#                 idx -=1

#             print("answer : ", answer)
#             print("count : ", count)
#             print("not_a_list : ", not_a_list)
#             print("idx : ", idx)

#             start = not_a_list[0]
#             end = not_a_list[-1]
#             to_left = length - start
#             to_right = length - 1 - count
#             to_right = end
#             # if idx < 1:
#             #     to_right = length - 1 - count
#             # else:
#             #     to_right = length - (length - 1 - idx)

#             print("to_right()() : ",  length - 1 - count, length - (length - 1 - idx))
#             left = idx-count
#             if left < 0:
#                 left = 0
#             right = length - 1 - idx 

#             # if name[-1] != 'A':
#             #     to_right = length-1
#                 # right += 1
#                 # left -= 1
            


#             print("start : ", start)
#             print("end : ", end)
#             print("to_left : ", to_left)
#             print("to_right : ", to_right)
#             print("left : ", left)
#             print("right : ", right)

#             # if left * 2 + right < to_left or left * 2 + right < to_right or right * 2 + left < to_left or right * 2 + left < to_right:
#             #     print("aaa")
#             #     if left > right:
#             #         answer += (2 * right + left)
#             #     else:
#             #         answer += (2 * left + right)
#             # else:
#             #     print("bbb")
#             #     answer += max(to_left, to_right)
#             answer += min(to_left, to_right, 2*left + right, 2*right + left)
#     return answer

# alphabet = [0] * 26
# for i in range(13):
#     alphabet[i] = i
#     alphabet[26-i-1] = i+1

# print("alphabet : ", alphabet)



# # name = "JEROEN" # 56
# # name = "JAN"
# # name = "ABAAAAAAAAABB"
# # name = "AAAAAAA" # 0
# # name = "ABAAAAAABAB" # 8
# # name = "ABABAAAAAAABA" # 10
# # name = "BBBBAABBB" # 15 # T5
# # name = "AABAAABAB" # 10

# # name = "AABAAABAB" # 10
# # name = "BABAAABAA" # 9

# # name = "AAABAABAB" # 9
# # name = "ZAAAZZZZZZZ" # 15
# # name = "ZZZZZZZAAAZ" # 16
# # name = "AAAZZZZZZZ" # 14
# name = "AAAZZZZZZZZ" # 16

# # name = "ABAAB" # 5

# # name = "BBBBAAAAB" # 10
# # name = "ZAAAZAAAAAA" # 6

# ###     

# # name ="ABAAAAAAAAABB" # 7
# # name ="AABAAAAAAABBB" # 11
# # name = "BBBAAB" # 8
# # name = "NNAAAAANNN" # 70 
# # name = "AAABBAAABBAAAAAAA" # 13
# # name = "AZAAAAAZZZAAA" # 12

# print(solution(name))



### 다른 사람 풀이
def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        print("num_char : ", num_char)
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx) # ?? (name[0] 에서 오른쪽으로 'A' 웅덩이를 만나기 전까지 길이와 name[-1]에서 왼쪽으로 'A' 웅덩이를 만나기 전까지 길이 중 최소 길이??)
        move = min(move, idx + n - next_idx + distance) # ?? (최소 움직임 계산??)
        print("idx | next_idx | distance | move : ", idx, next_idx, distance, move)

    answer += move
    return answer

name = "AZAAAAAZZZAAA" # 12
print(solution(name))