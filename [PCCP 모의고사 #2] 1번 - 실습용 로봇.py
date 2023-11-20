def solution(command):
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    dir = 0
    r, c = 0, 0
    for co in command:
        if co == 'R':
            dir = (dir + 1) % 4
        elif co == 'L':
            dir = (dir - 1) % 4
        elif co == 'G':
            r = r + dr[dir]
            c = c + dc[dir]
        else:
            r = r - dr[dir]
            c = c - dc[dir]

    return [r, c]


print(solution("GRGLGRG"))
