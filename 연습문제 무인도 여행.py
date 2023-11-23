from collections import deque


def solution(maps):
    global answer

    def bfs(r, c, visited, zido):
        global answer
        q = deque([])
        visited[r][c] = 1
        q.append((r, c))
        dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
        num = zido[r][c]
        while q:
            tr, tc = q.popleft()
            for i in range(4):
                new_r, new_c = tr + dr[i], tc + dc[i]
                if new_r < 0 or new_r >= len(visited) or new_c < 0 or new_c >= len(visited[0]):
                    continue
                if zido[new_r][new_c] == 0:
                    continue
                if visited[new_r][new_c] == 1:
                    continue
                visited[new_r][new_c] = 1
                num += zido[new_r][new_c]
                q.append((new_r, new_c))
        answer.append(num)
        return visited

    answer = []
    zido = []
    for m in maps:
        temp = []
        for x in m:
            if x == 'X':
                temp.append(0)
            else:
                temp.append(int(x))
        zido.append(temp)

    visited = [[0 for _ in range(len(zido[0]))] for _ in range(len(zido))]

    for i in range(len(zido)):
        for j in range(len(zido[0])):
            if visited[i][j] == 0 and zido[i][j] != 0:
                visited=bfs(i, j, visited, zido)
    if not answer:
        answer=[-1]
    else:
        answer.sort()
    return answer

a=solution(["X591X","X1X5X","X231X", "1XXX1"])