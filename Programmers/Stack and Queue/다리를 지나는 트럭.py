## 0) 실패

# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     truck_weights = deque(truck_weights)
#     # print("truck_weights : ", truck_weights)
#     time = 0
#     # current_weight = 0
#     trucks = deque()
#     flag = True
#     while truck_weights:
        
#         print("trucks_A : ", trucks)
        
#         while True:
            
#             if truck_weights and sum(trucks) + truck_weights[0] <= weight:
#                 trucks.append(truck_weights.popleft())
#                 time+= 1
#                 print("trucks_B : ", trucks)
#             else:
#                 break



#         if len(trucks) == 2:
#             flag = False
#         else: 
#             flag = True

#         if flag:
#             time += bridge_length - len(trucks) +1
#         else:
#             time += 1
        
#         trucks.popleft()



#         print("time : ", time, truck_weights, trucks)
#         print()
        

        
        
#     return answer

### 1) 실패 64.3 / 100
# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     # answer = 0
#     truck_weights = deque(truck_weights)
#     # print("truck_weights : ", truck_weights)
#     time = 0
#     # current_weight = 0
#     trucks = deque([0] * bridge_length)
#     flag = True
#     print("trucks_A : ", trucks)
#     # while truck_weights:                        
#     while True:            
#     # for i in range(1, 10):
#         print()
#         print("aaa : ", truck_weights)
#         if truck_weights:
#             if sum(trucks) + truck_weights[0] <= weight:
#                 trucks.popleft()
#                 trucks.append(truck_weights.popleft())
#                 time += 1
#                 print("trucks_B : ", trucks)
#             else:
#                 print('bbb_a : ', trucks)
#                 # while trucks[0] == 0:
#                 #     trucks.popleft()
#                 #     trucks.append(0)
#                 #     time += 1                
                
#                 # if trucks[0] == 0:
#                 #     time += 1
           

#                 trucks.popleft()
#                 trucks.append(0)
#                 if sum(trucks) + truck_weights[0] > weight:
#                     time += 1
            
                
#                 # time+=1
#                 print('bbb_b : ', trucks)
#         else:
#             print("b")
#             print(trucks)
#             while trucks:
#                 # print("c")
#                 trucks.popleft()
#                 time += 1
#             break

#         print("time : ", time)

#     return time

# ### 2) 오답..
# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     truck_weights = deque(truck_weights)
#     time = 0
#     bridges = deque([0] * bridge_length)                  
#     count = 0
#     while bridges:            
#     # for i in range(1, 10):
#         print()
#         print("aaa : ", truck_weights)
#         if truck_weights:
#             if count + truck_weights[0] <= weight:
#                 bridge = bridges.popleft()
#                 truck = truck_weights.popleft()
#                 bridges.append(truck)
#                 count -= bridge
#                 count += truck
#                 time += 1
#                 print("trucks_B : ", bridges)
#             else:
#                 print('bbb_a : ', bridges)
        
#                 if count + truck_weights[0] > weight:
#                     bridge = bridges.popleft()
#                     count -= bridge
#                     bridges.append(0)
#                     time += 1
            
                
#                 # time+=1
#                 print('bbb_b : ', bridges)
#         else:
#             print("b")
#             print(bridges)
#             while bridges:
#                 # print("c")
#                 bridges.popleft()
#                 time += 1
#             break

#         print("time : ", time)

#     return time


### 3) 정답..
def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    while len(trucks_on_bridge):
        print("trucks_on_bridge : ", trucks_on_bridge)
        answer += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
    return answer


# bridge_length = 2
# weight = 10
# truck_weights = [7, 4, 5, 6]
# # 8

# bridge_length = 4
# weight = 10
# truck_weights = [7, 2, 5, 2, 1]
# # 11

# bridge_length = 100
# weight = 100
# truck_weights = [10]
# # 101

# bridge_length = 100
# weight = 100
# truck_weights = [10,10,10,10,10,10,10,10,10,10]
# 110

# bridge_length = 5
# weight = 5
# truck_weights = [2, 2, 2, 2, 1, 1, 1, 1, 1]
## 19

# bridge_length = 1
# weight = 2
# truck_weights = [1, 1, 1]	
# # 4

# bridge_length = 1
# weight = 1
# truck_weights = [1, 1, 1]	
# # 4

# bridge_length = 4
# weight = 2
# truck_weights = [1, 1, 1, 1]	
# # 10

# bridge_length = 3
# weight = 3
# truck_weights = [1, 1, 1]
# # 6

# bridge_length = 3
# weight = 1
# truck_weights = [1, 1, 1]
# # 10

bridge_length = 5
weight = 5
truck_weights = [1, 1, 1, 1, 1, 2, 2]
# 14

print(solution(bridge_length, weight, truck_weights))