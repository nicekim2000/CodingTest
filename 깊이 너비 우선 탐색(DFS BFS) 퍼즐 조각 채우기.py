from collections import deque
def solution(game_board, table):
    def left_push(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n - 1):
                matrix[i][j] = matrix[i][j + 1]
            matrix[i][n - 1] = 0
        return matrix
    def up_push(matrix):
        n = len(matrix)
        for j in range(n):
            for i in range(1, n):
                matrix[i - 1][j] = matrix[i][j]
            matrix[n - 1][j] = 0
        return matrix
    def move2(matrix):
        while sum(x[0] for x in matrix)==0:
            matrix=left_push(matrix)
        while sum(matrix[0])==0:
            matrix=up_push(matrix)


        return matrix
    def move(group):
        min_r=min(x[0] for x in group)
        max_r=max(x[0] for x in group)
        min_c=min(x[1] for x in group)
        max_c=max(x[1] for x in group)
        size=max(max_r-min_r,max_c-min_c)+1
        arr=[[0 for _ in range(size)]for _ in range(size)]
        for g in group:
            r,c=g
            arr[r-min_r][c-min_c]=1
        return arr

    def bfs(r,c,visited,zido,value):
        group=[[r,c]]
        q=deque([])
        q.append([r,c])
        visited[r][c]=1
        dr,dc=[0,0,1,-1],[-1,1,0,0]
        while q:
            nr,nc=q.popleft()
            for i in range(4):
                new_r,new_c=nr+dr[i],nc+dc[i]
                if new_r < 0 or new_c >= length or new_c < 0 or new_r >= length:
                    continue
                if visited[new_r][new_c]==1 : continue
                if zido[new_r][new_c]==value : continue
                visited[new_r][new_c]=1
                group.append([new_r,new_c])
                q.append([new_r,new_c])


        return visited,move(group)
    def rotate(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix
    def same(arr1,arr2):
        le=len(arr1)
        cnt=0
        for i in range(le):
            for j in range(le):
                if arr1[i][j]!=arr2[i][j]:
                    return 0
                if arr1[i][j]==1:
                    cnt+=1
        return cnt

    g,t=[],[]
    answer = 0
    length=len(game_board)
    visited1=[[0 for _ in range(length)] for _ in range(length)]
    visited2=[[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            if game_board[i][j]==0 and visited1[i][j]==0 :
                visited1,temp=bfs(i,j,visited1,game_board,1)
                ttemp=[temp,0]
                g.append(ttemp)
            if table[i][j]==1 and visited2[i][j]==0:
                visited2,temp = bfs(i, j, visited2, table, 0)
                t.append(temp)
    for target in t:
        for origin in g:

            if len(origin[0])!=len(target) or origin[1]==1 : continue
            value=same(target,origin[0])
            if value > 0 :
                answer+=value
                origin[1]=1
                break
            temp=target[:]
            for _ in range(3):
                temp=rotate(temp)
                ttemp=move2(temp)
                value=same(ttemp,origin[0])
                if value > 0 :
                    origin[1] = 1
                    answer+=value
                    break
            if value > 0 :
                break

    return answer


a=solution([[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
,[[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]])
print(a)