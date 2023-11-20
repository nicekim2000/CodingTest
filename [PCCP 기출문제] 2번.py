def solution(land):
    def bfs(visited, r, c,num,land):
        q = []
        visited_list = []
        q.append((r, c))
        visited_list.append((r, c))
        visited[r][c] = 1
        land[r][c]=num
        dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
        while q:
            nr, nc = q.pop(0)
            for i in range(4):
                new_r, new_c = nr + dr[i], nc + dc[i]
                if new_r < 0 or new_r >= len(land) or new_c < 0 or new_c >= len(land[0]):
                    continue
                if visited[new_r][new_c] >= 1: continue
                if land[new_r][new_c] == 0: continue
                land[new_r][new_c]=num
                q.append((new_r, new_c))
                visited_list.append((new_r, new_c))
                visited[new_r][new_c] = 1
        for r, c in visited_list:
            visited[r][c] = len(visited_list)
        return visited,land

    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    num=2
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and visited[i][j] == 0:
                visited,land = bfs(visited, i, j,num,land)
                num+=1

    answer = []
    for i in range(len(land[0])):
        temp = 0
        dup=[]
        for j in range(len(land)):
            if land[j][i]>=2 and land[j][i] not in dup:
                dup.append(land[j][i])
                temp += visited[j][i]
        answer.append(temp)
    return max(answer)