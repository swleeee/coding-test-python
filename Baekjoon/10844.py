import sys
input = sys.stdin.readline

n = int(input())
array = [[0] * 10 for _ in range(n)]

array[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            array[i][j] = array[i-1][1]
        elif j == 9:
            array[i][j] = array[i-1][8]
        else:
            array[i][j] = array[i-1][j-1] + array[i-1][j+1]

# print("array : ", array)
print(sum(array[n-1]) % 10 ** 9)