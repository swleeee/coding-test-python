# n = list(map(int, input().split()))

# print(n)
sum_element = -1
count_ary = []

# print(sum(n))

while sum_element != 0:
    # print("sum_element", sum_element)
    data = list(map(int, input().split()))
    sum_element = sum(data)
    count = 0
    if(sum_element):
        count += (data[2] // data[1]) * data[0]
        if(data[2] % data[1] < data[0]):
            count += data[2] % data[1]
        else:
            count += data[0]
        count_ary.append(count)


# print(count_ary)

for i in range(len(count_ary)):
    print("Case ", i+1,": ",count_ary[i], sep="")


## list 말고 개별 값으로 받아서 처리하는 것이 더 효율적일 거 같음