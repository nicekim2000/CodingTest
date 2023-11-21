def solution(board):
    def check(i, j, visited, n):
        visited[i][j] = 1
        dr, dc = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
        for idx in range(8):
            new_i = dr[idx] + i
            new_j = dc[idx] + j
            if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n:
                continue
            visited[new_i][new_j] = 1
        return visited

    n = len(board)
    full = n * n
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                visited = check(i, j, visited, n)
    value = sum([sum(x) for x in visited])


    return full-value

a=solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])
print(a)