### 1) 시간 복잡도 ㅠㅠ..
# def solution(number, k):
#     answer = ''
#     length = len(number)
#     # print("number[0] | length : ", number[0], length)
#     k = int(k)
#     start = 0
#     end = k
#     digit = length - k
#     # print("aaa : ", max(number[start:end+1]))
#     # for i in range(k):
        
#     # for i, num in enumerate(number):
#     #     print("bbb : ", i, num)
    
#     while k > 0:
#         # print("ccc : ", number, start, end+1)
#         max_value = max(number[start:end+1])
#         count = 0
#         for i in range(start, end+1):
#             if number[i] == max_value:
#                 k -= count
#                 end += 1
#                 start += count + 1
#                 answer += max_value
#                 digit -= 1
#                 max_value = -1                
#                 break
#             else:
#                 count += 1
#             print("max_value | count | start | end | answer : ", max_value, count, start, end, answer)

#         if digit < 1:
#             start = length
#             break

#     if start != length:
#         answer += number[start:]


#     return answer

### 2) 오답
# def make_digit(num, k):

# def solution(number, k):
#     # answer = []
    
  
#     k = int(k)
#     # max_value = -1
#     # digit = number
   

#     # for i, num in enumerate(number):
#     #     if num > max_value:
#     #         max_value = num

#     # while k > 0:
#     #     make_digit(number, k)

#     # num = number
#     while k > 0:
#         print("number : ", number)
#         length = len(number)
#         c = ""
#         for i in range(length):
#             if k < 1:
#                 c += number[i]

#             elif i != length -1:
#                 # if number[i] == '9':
#                 #     c += number[i]
#                 if number[i] >= number[i+1]:
#                     c += number[i]        
#                 else:
#                     k -= 1


#             print("c : ", c)  

#         print("bbb : ", k)
#         if k > 0:
#             c += number[-1]


#         if number == c:
#             number = number[:len(number)-k]
#             break
#         number = c
#         # if 
#         # k -= 5
            


#     return number

### 3) ㅠㅠ
# def solution(number, k):

#     k = int(k)
#     print("before : ", number)
#     # str.replace(number[0], "")
#     # number = number[:1] + number[2:]
#     temp = 3
#     while k > 0:
#         if temp < 1:
#             break
#         length = len(number)
#         print("length : ", length)
#         for i in range(length-1):
            
#             print("aaa : ", i)
#             if number[i] < number[i+1]:
#                 number = number[:i] + number[i+1:]
#                 k -= 1
#                 break
#         temp -= 1


#     print("after : ", number)

#     return number

# ### 4)
# def solution(number, k):
#     answer = ''
#     length = len(number)
#     # print("number[0] | length : ", number[0], length)
#     k = int(k)
#     start = 0
#     end = k
#     digit = length - k

#     while k > 0:
       
#         max_value = max(number[start:end+1])

#         idx = number[start:end+1].find(max_value)
#         k -= (idx - start)
#         end += 1
#         start += idx + 1
#         answer += max_value
#         digit -= 1
        
#         # print("max_value | start | end | answer | idx : ", max_value, start, end, answer, idx)
#         max_value = -1

#         if digit < 1:
#             start = length
#             break

#     if start != length:
#         answer += number[start:]


#     return answer

### 4) 정답.. 휴
# def solution(number, k):
#     answer = ''
#     length = len(number) - int(k)
#     start = 0
#     end = int(k) + 1
#     max_value = -1
#     max_index = -1

#     while length > 0:        
#         a = number[start:end]
#         # print("start | end | a : ", start, end, a)
#         for i, num in enumerate(a):
#             if num == '9':
#                 answer += num                
#                 start += i+1
#                 end += 1    
#                 break
#             elif int(num) > int(max_value):
#                 max_value = num
#                 max_index = i

#         # print("num : ", num, answer, max_value) 
#         if num != '9':
#             # print('bbb')
#             answer += max_value
#             start += max_index + 1
#             end += 1
        
#         # print("answer : ", answer)
#         max_value = -1
#         length -= 1

    

#         print("max_value | start | end | answer | a | length : ", max_value, start, end, answer, a, length)
#     if len(number) - int(k) != len(answer):
#         # print("ddd")
#         answer += number[-1]

#     # print('ccc : ', answer)
#     return answer

### 5) 다른 사람 풀이 1. 스택 활용

def solution(number, k):
    stack = [number[0]]
    print('stack : ', stack)
    for num in number[1:]:
        print("num : ", num)
        while len(stack) > 0 and stack[-1] < num and k > 0:
        
            k -= 1
            print("before : ", stack)
            stack.pop()
            print("after : ", stack)
        stack.append(num)
        print("stack | num | k : ", stack, num, k)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

number = "4177252841"
k = 4

# number = "1924"
# k = "2"

# number = "1231234"
# k = "3"

# number = "1231234"
# k = "0"

# number = "9998887776665554443332221110009"
# k = "30"

# number = "9" * 10**6
# k = "500000"

# number = "1000"
# k = "3"

# number = "10502"
# k = "2"


print(solution(number, k))