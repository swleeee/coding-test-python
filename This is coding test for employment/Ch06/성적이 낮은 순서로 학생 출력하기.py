# n = int(input())

# data = [list(map(str, input().split())) for _ in range(n)]

# print(data)

# ary = sorted(data, key= lambda x:x[1])

# print(ary)

# for student in ary:
#     print(student[0], end=' ')




### 해설 
n = int(input())

array = []
for i in range(n):
    input_data = input().split()

    array.append((input_data[0], int(input_data[1])))


array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end= ' ')