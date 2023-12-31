from collections import deque
def bfs(zido,characterX, characterY, itemX, itemY,max_x,max_y):
    cnt=0
    q=deque([[characterX, characterY,cnt]])
    visited=[[0 for _ in range(max_x)] for _ in range(max_y)]
    visited[characterY][characterX]=1
    zido[characterY][characterX]=1
    dx,dy=[0,1,-1,0],[1,0,0,-1]
    fx,fy=[0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]
    while q:
        x,y,ccnt=q.popleft()
        # print(x,y,ccnt)
        if (x,y)==(itemX,itemY):
            return ccnt
        for i in range(4):
            new_x,new_y=x+dx[i],y+dy[i]
            edge=False
            if new_x < 0 or new_x >= max_x or new_y < 0 or new_y >= max_y :
                continue
            if visited[new_y][new_x]==1 or zido[new_y][new_x]==0: continue
            for j in range(8):
                temp_x,temp_y=new_x+fx[j],new_y+fy[j]
                if temp_x < 0 or temp_x >= max_x or temp_y < 0 or temp_y >= max_y:
                    continue
                if zido[temp_y][temp_x]==0:
                    edge=True
                    break
            if not edge : continue
            visited[new_y][new_x]=1
            zido[new_y][new_x]=ccnt+1
            q.append([new_x,new_y,ccnt+1])
def solution(rectangle, characterX, characterY, itemX, itemY):
    max_x=(max(x[2] for x in rectangle)+1)*2+1
    max_y = (max(x[3] for x in rectangle)+1)*2+1
    # print(max_x,max_y)
    zido=[[0 for _ in range(max_x)] for _ in range(max_y)]
    # print(zido)
    for r in rectangle:
        for y in range(r[1]*2, r[3]*2+1):
            for x in range(r[0]*2,r[2]*2+1):
                zido[y][x]=1
        # for i in range(max_y*2):
        #     print(zido[max_y - 1 - i])
        # print()
    # for i in range(max_y):
    #     print(zido[max_y-1-i])
    answer=bfs(zido, characterX*2, characterY*2, itemX*2, itemY*2,max_x,max_y)
    # for i in range(max_y):
    #     print(zido[max_y-1-i])

    return answer//2



a=solution(	[[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)
print(a)