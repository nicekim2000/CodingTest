from collections import deque
import heapq
# 상,좌,우,하 방향으로 탐색
def find_people(r,c):
    if (r,c) in people:
        return 0,r,c
    visited=[[0 for _ in range(n)]for _ in range(n)]
    visited[r][c]=1
    q=deque([])
    ll=[]
    q.append([r,c,0])
    dr,dc=[-1,0,1,0],[0,-1,0,1]
    max_dist=n*n+1
    while q:
        nr,nc,nd=q.popleft()
        if nd>=max_dist: continue
        for i in range(4):
            new_r,new_c=nr+dr[i],nc+dc[i]
            if (new_r,new_c) in people:
                if nd+1<=max_dist:
                    max_dist=nd+1
                    heapq.heappush(ll,(nd+1,new_r,new_c))
                    # print(new_r,new_c,nd+1)
                    continue
                return nd+1,new_r,new_c
            if new_r < 0 or new_r >=n or new_c < 0 or new_c >= n : continue
            if visited[new_r][new_c]==1 or zido[new_r][new_c]==1: continue
            visited[new_r][new_c]=1
            q.append([new_r,new_c,nd+1])
    if not ll:
        return -1,0,0
    else:
        return heapq.heappop(ll)
def find_dest(r,c,dest_r,dest_c):
    visited=[[0 for _ in range(n)]for _ in range(n)]
    visited[r][c]=1
    q=deque([])
    q.append([r,c,0])
    dr,dc=[-1,0,1,0],[0,-1,0,1]

    while q:
        nr,nc,nd=q.popleft()
        for i in range(4):
            new_r,new_c=nr+dr[i],nc+dc[i]
            if (new_r,new_c) == (dest_r,dest_c):
                return new_r,new_c,nd+1
            if new_r < 0 or new_r >=n or new_c < 0 or new_c >= n : continue
            if visited[new_r][new_c]==1 or zido[new_r][new_c]==1: continue
            visited[new_r][new_c]=1
            q.append([new_r,new_c,nd+1])
    return 0,0,-1

n,m,fuel=map(int,input().split())
zido=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    zido.append(temp)
me=list(map(int,input().split()))
me[0],me[1]=me[0]-1,me[1]-1
people={}
for _ in range(m):
    p=list(map(int, input().split()))
    people[(p[0]-1,p[1]-1)]=(p[2]-1,p[3]-1)


for _ in range(m):
    dist,me[0],me[1]=find_people(me[0],me[1])
    if fuel < dist or dist==-1:
        print(-1)
        exit()
    else :
        fuel-=dist
    # print(me)
    dest=people[(me[0],me[1])]
    del people[(me[0],me[1])]
    if me[0]==dest[0] and me[1]==dest[1]:
        dist=0
    else:
        me[0],me[1],dist=find_dest(me[0],me[1],dest[0],dest[1])
    if fuel < dist or dist==-1:
        print(-1)
        exit()
    fuel+=dist
print(fuel)


