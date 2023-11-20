from collections import deque


def solution(n, m, hole):
    visited = [[[0]*2 for _ in range(n)] for _ in range(m)]
    for hc, hr in hole:
        hc -= 1
        hr = m - hr
        visited[hr][hc][0] = -1
        visited[hr][hc][1] = -1


    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

    q = deque([])
    count = 0
    q.append([m - 1, 0, count, 0])
    visited[m - 1][0][0] = 1
    while q:
        r, c, cnt,used = q.popleft()
        if r==0 and c==n-1 :
            return cnt
        for i in range(4):
            new_r, new_c = r + dr[i], c + dc[i]
            if new_r < 0 or new_r >= m or new_c < 0 or new_c >= n: continue
            if visited[new_r][new_c][0]==-1 : continue
            if visited[new_r][new_c][0] == 1 : continue
            visited[new_r][new_c][0]=1
            q.append([new_r,new_c,cnt+1,used])
        if not used:
            for i in range(4):
                new_r, new_c = r + dr[i]*2, c + dc[i]*2
                if new_r < 0 or new_r >= m or new_c < 0 or new_c >= n: continue
                if visited[new_r][new_c][1] == -1: continue
                if visited[new_r][new_c][1] == 1: continue
                visited[new_r][new_c][1] = 1
                used=1
                q.append([new_r, new_c, cnt + 1, used])
    return -1
    # for i in range(m):
    #     print(visited[i])
    # if visited[0][n-1]==m*n+1 : return -1
    # else : return visited[0][n-1]


print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))
