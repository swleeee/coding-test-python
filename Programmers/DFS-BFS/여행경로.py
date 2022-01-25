from collections import defaultdict

def solution(tickets):
    answer = []
    dict = defaultdict(list)
    
    for ticket in tickets:
        dict[ticket[0]].append(ticket[1])

    for key in dict.keys():
        dict[key].sort(reverse=True)

    print(dict)
    stack = ["ICN"]
    
    while stack:
        print("before : ", stack)
        start = stack[-1]



        if not dict[start]:
            answer.append(stack.pop())
        else:
            stack.append(dict[start].pop())
        print("after : ", stack)
        print("answer | dict : ", answer, dict)
        print()
    answer.reverse()


    return answer

# tickets= [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
print(solution(tickets))