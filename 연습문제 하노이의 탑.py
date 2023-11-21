def solution(n):
    # [[1,3],[1,2],[3,1],[2,3],[1,3]]
    answer = []

    def dfs(s, t, mid, n):
        if n == 1:
            answer.append([s, t])
        else:
            dfs(s, mid, t, n - 1)
            dfs(s, t, mid, 1)
            dfs(mid,t,s,n-1)
    dfs(1,3,2,n)


    return answer

a=solution(3)
print(a)