from collections import deque

### 1) 효율 x and 오답
# def solution(people, limit):
#     # answer = 0
    
#     # people.sort(reverse=True)
#     people = deque(sorted(people))
#     print("people : ", people)
#     count = 0
#     while people:
#         man = people.popleft()
#         on_load = []    
        


#         for i, person in enumerate(people):
#             if man + person <= limit:
#                 man += person
#                 on_load.append(i)
        
#         if on_load:
#             while on_load:
#                 a = on_load.pop()
#                 del people[a]

#         count += 1
#         # print("people : ", people, on_load, man)
    
#     # print('count : ', count)
#     return count

### 2)
def solution(people, limit):
    people = deque(sorted(people))
    count = 0
        
    while people:
        if len(people) == 1:
            count += 1
            break
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        else:
            people.pop()

        count += 1

        print("people : ", people, count)
    
    return count


# people=[70, 50, 80, 50]
# limit = 100
## 3

# people=[70, 50, 80]
# limit = 100
## 3

people=[40, 40, 50, 60, 70]
limit = 140
## 2

# people=[40, 50, 150, 160]
# limit = 200 
## 2

# people=[100, 500, 500, 900, 950]
# limit = 1000
## 3

print(solution(people, limit))