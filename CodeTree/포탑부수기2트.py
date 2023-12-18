

import heapq
from collections import deque

# 우하좌상
def bfs(ar,ac,dr,dc):
    prev={}
    visited=[[0 for _ in range(n)] for _ in range(m)]
    visited[ar][ac]=1
    q=deque([])
    q.append((ar,ac))

    mr,mc=[0,1,0,-1],[1,0,-1,0]
    path=[]
    while q:
        nr,nc=q.popleft()
        for i in range(4):
            new_r,new_c=(nr+mr[i])%n,(nc+mc[i])%m
            if new_r==dr and new_c==dc :
                path.append((new_r,new_c))
                path.append((nr,nc))
                while True:
                    nr,nc=prev[(nr,nc)]
                    path.append((nr,nc))
                    if (nr,nc)==(ar,ac) : break
                return path
            if new_r < 0 or new_r >= m or new_c < 0 or new_c >=n : continue
            if zido[new_r][new_c]<=0 or visited[new_r][new_c]==1: continue
            visited[new_r][new_c]=1
            q.append((new_r,new_c))
            prev[(new_r,new_c)]=(nr,nc)
    return path







n,m,k=map(int,input().split())
zido=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    zido.append(temp)

top={}
hq=[]
for i in range(m):
    for j in range(n):
        if zido[i][j]>0:

            heapq.heappush(hq,(zido[i][j],0,-(i+j),-j))
            top[(i,j)]=[zido[i][j],1]
print(hq)

for _ in range(k):

    attacker=hq[0][:]
    defender=hq[-1][:]
    print(attacker)
    ar,ac=-attacker[2]+attacker[3],-attacker[3]
    dr,dc=-defender[2]+defender[3],-defender[3]
    attack_value=attacker[0]+n+m
    half_attack_value=attack_value//2

    path=bfs(ar,ac,dr,dc)
    print(path)
    if not path:
        path.append((ar,ac))
        path.append((dr,dc))
        move_r,move_c=[-1,-1,-1,0,1,1,1,0],[-1,0,1,1,1,0,-1,-1]
        for i in range(8):
            new_r,new_c=(dr+move_r[i])%m,(dc+move_c[i])%n
            if (new_r,new_c)==(ar,ac): continue
            zido[new_r][new_c]-=half_attack_value
            path.append((new_r,new_c))
    else:
        for i in range(len(path)-2,0,-1):
            zido[path[i][0]][path[i][1]]-=half_attack_value
    zido[path[0][0]][path[0][1]]-=attack_value
    remain_list=set(list(top.keys()))-set(path)
    print(remain_list)