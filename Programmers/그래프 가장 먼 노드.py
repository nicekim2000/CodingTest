from collections import deque
def solution(n, edge):
    answer = 0
    graph=[[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    inf=1e9
    cost=[inf for _ in range(n+1)]
    cost[1]=0
    q=deque([])
    for e in graph[1]:
        q.append(e)
        cost[e]=1
    while q:
        temp=q.popleft()
        for num in graph[temp]:
            if cost[temp]+1<cost[num]:
                q.append(num)
                cost[num]=cost[temp]+1

    max_cnt=max(cost[1:])
    for i in range(1,n+1):
        if max_cnt==cost[i]:
            answer+=1
    return answer

a=solution(	6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
print(a)
