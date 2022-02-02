INF = int(1e9)

def solution(n, results):
    answer = 0
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a==b:
                graph[a][b] = 0

    for a, b in results:
        graph[a][b] = 1


    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    print("graph : ", graph)
    for a in range(1, n+1):
        count = 0
        for b in range(1, n+1):
            if graph[a][b] != INF or graph[b][a] != INF:
                count += 1
                
        print("aaa : ", a, b, count, n)
        if count == n:
            answer +=1

    return answer

n = 5
results=[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	

print(solution(n, results))