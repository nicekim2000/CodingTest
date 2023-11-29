def solution(info, edges):
    global answer

    def check(cur, gogo):
        new_go = [x for x in gogo if x != cur]
        if cur in graph:
            new_go+=graph[cur]
        return new_go

    def dfs(cur, sheep, wolf, gogo):
        global answer
        # print(cur,sheep,wolf,gogo,answer)
        if sheep == wolf:
            if answer < sheep :
                answer = sheep
            return
        new_go=check(cur, gogo)
        if not new_go:
            if answer < sheep:
                answer = sheep
            return
        for g in new_go:
            if info[g]==0:
                dfs(g,sheep+1,wolf,new_go)
            else:
                dfs(g,sheep,wolf+1,new_go)



    answer = 1
    graph = {}
    for e in edges:
        if e[0] not in graph:
            graph[e[0]]=[e[1]]
        else:
            graph[e[0]].append(e[1])
    dfs(0, 1, 0, [0])
    # print(answer)
    return answer

a=solution(	[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]])
