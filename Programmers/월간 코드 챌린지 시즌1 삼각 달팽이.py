def solution(n):
    answer = []
    value=0
    for i in range(1,n+1):
        value+=i
    zido=[[0 for _ in range(n)]for _ in range(n)]
    turn=0
    cnt=0
    thr=n
    r,c=0,0
    dir=[[1,0],[0,1],[-1,-1]]
    for i in range(1,value+1):
        zido[r][c]=i
        cnt+=1
        if cnt==thr:
            turn=(turn+1)%3
            cnt=0
            thr-=1
        r=r+dir[turn][0]
        c=c+dir[turn][1]

    for i in range(n):
        for j in range(n):
            if zido[i][j]!=0:
                answer.append(zido[i][j])
    return answer