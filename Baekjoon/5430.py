import sys
from collections import deque
sys.stdin.readline

t = int(input())

for a in range(t):
    error = False
    f_list = list(input())
    n = int(input())    
    # d = input()
    data = input()[1:-1].split(",")

    # if len(d) > 2:
    #     data = deque(map(int, d.replace('[', '').replace(']', '').split(
    #         ',')))
    #     # data = d[1:-1].split(',')    
    # else:
    #     data= []
    if data[0] != '':
        data = deque(data)
    else:
        data = deque()
        
    r_count = 0
    # d_count = 0
    
    for func in f_list:
        # print("data", a, data)
        if(func == 'R'):
            r_count += 1        
        else:            
            # if('' in data): 
            #     print("error")                   
            #     error = True
            #     break
                # data.clear()
            if(len(data) > 0):                
                if(r_count % 2 == 1):
                    data.pop()
                else:                    
                    data.popleft()

            else:                    
                # answer.append("error")
                error = True
                print("error")
                # type_list.append(True)
                break

    # if('' in data):            
    #     # data.clear()
    #     error = True
    #     print("[]")
    #     break
    # if(a == len(answer)):
    
    if(not error):
        # answer.append(data)
        if(r_count % 2 == 1):
            # type_list.append(False)
            data.reverse()
            print('[', end='')               
            print(','.join(map(str, data)), end='')
            print(']')
            # print('['+ ','.join(data[::-1]) + ']')
        else:
            print('[', end='')               
            print(','.join(map(str, data)), end='')
            print(']')
            # print('['+ ','.join(data) + ']')
            # type_list.append(True)    