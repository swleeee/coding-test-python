# n = int(input())

# ary = []

# for i in range(n):
#     input_data = input().split()

#     ary.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))


# # print("ary : ", ary)

# processed_ary = sorted(ary, key=lambda x: (-x[1], x[2], -x[3], x[0]))



# print("processed_ary : ", processed_ary)




### 풀이
n = int(input())
students = [] # 학생 정보를 담을 리스트

for _ in range(n):
    students.append(input().split())

students.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])

## Input Data
# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90