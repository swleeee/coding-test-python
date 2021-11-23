import sys
input = sys.stdin.readline

n = int(input())
ary = []
# length_list = []
# char_list = []
# char_idx_list = []
card_idx = 9
dic={}

for i in range(n):
    s = input().rstrip()    
    ary.append(list(s))
     
    for i in range(len(s)):
        # print("sub_s", s[i])

        ## 각 단어의 자릿수 가중치만큼 dic에 저장
        if s[i] in dic:
            dic[s[i]] += 10 ** (len(s)-1-i)
        else:
            dic[s[i]] = 10 ** (len(s)-1-i)

## 각 단어의 자릿수 가중치 정렬
sorted_ary = sorted(dic.items(), key=(lambda x:x[1]), reverse=True)

#print(sorted_ary)

count = 0

# for i in range(len(sorted_ary)):
#     count += 


## 자릿수 가중치가 높은 순서대로 (9, 8, ..., 1) 곱해서 더함
for s in sorted_ary:
    count += s[1] * card_idx
    card_idx -= 1

print(count)




###### 잘못 생각한 로직

# for i in range(n):
#     for j in range(len(ary[i])):
#         print("ccc", ary[i][j], char_list)
#         if ary[i][j] in char_list:            
#             continue
#         else:
#             char_list.append(ary[i][j])
#             char_idx_list.append(list(ary[i][j] + str(len(ary[i])-j)))
#             # print("ddd", list(ary[i][j] + str(len(ary[i])-j)))

# char_idx_list.sort(key=lambda x: -int(x[1]))

# for s in char_idx_list:
#     s[1] = card_idx
#     # print("s[1]", s[1])    
#     for i in range(n):
#         ary[i] = ''.join(ary[i])
#         # print("hhh", s[0] in ary[i])
#         if s[0] in ary[i]:
#             print("ary", ary[i], i, s[0], s[1], type(ary[i]))            
#             ary[i]= ary[i].replace(s[0], str(s[1]))
#             print("dd", ary)
#     card_idx -= 1

# count = 0
# for s in ary:
#     count += int(s)

# print(count)