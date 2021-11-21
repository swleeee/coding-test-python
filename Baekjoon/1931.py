import sys
input = sys.stdin.readline


n = int(input())
ary=[]
count = 0

for i in range(n):    
    b = []
    b = list(map(int, input().split()))
    b.append(b[1]-b[0])   
    ary.append(b)

ary.sort(key=lambda x:(x[1], -x[2]))

# print("ary", ary)
line_list = [-1, -1]
for s in ary:
    if(line_list[0] == -1):
        line_list[0] = s[0]
        line_list[1] = s[1]
        count += 1
    else:        
        if line_list[1] <= s[0]:
            line_list[1] = s[1]
            count += 1
    # print(line_list, count)
        
print(count)