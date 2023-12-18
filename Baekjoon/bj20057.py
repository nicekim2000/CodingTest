from collections import deque
def turning(wzido):
    temp = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp[i][j]=wzido[j][4-i]
    return temp
def wz(v):
    wzido=[[0 for _ in range(5)]for _ in range(5)]

    wzido[2][0]=int(v*0.05)
    wzido[1][1],wzido[3][1]=int(v*0.1),int(v*0.1)
    wzido[1][2],wzido[3][2]=int(v*0.07),int(v*0.07)
    wzido[0][2],wzido[4][2]=int(v*0.02),int(v*0.02)
    wzido[1][3],wzido[3][3]=int(v*0.01),int(v*0.01)
    new_v=v-int(v*0.05)-int(v*0.1)-int(v*0.1)-int(v*0.02)-int(v*0.02)-int(v*0.01)-int(v*0.01)-int(v*0.07)-int(v*0.07)
    wzido[2][1] = new_v
    return wzido

def wind(pos,dir):
    global zido,out
    wind_zdio=wz(zido[pos[0]][pos[1]])
    zido[pos[0]][pos[1]]=0
    for _ in range(dir):
        wind_zdio=turning(wind_zdio)
    for r in range(5):
        for c in range(5):
            if r-2+pos[0] < 0 or r-2+pos[0] >= n or c-2+pos[1] < 0 or c-2+pos[1] >=n :
                out+=wind_zdio[r][c]
            else :
                zido[r-2+pos[0]][c-2+pos[1]]+=wind_zdio[r][c]

n=int(input())
zido=[]
for _ in range(n):
    zido.append(list(map(int,input().split())))

mid=n//2
turn=[]
left_pos=[n//2,n//2-1]
mid_pos=[n//2,n//2]
dr,dc=[1,1,-1],[-1,1,1]

for i in range(1,mid+1):
    turn.append([left_pos[0] + (-1 * (i - 1)), left_pos[1] + (-1 * (i - 1))])
    for j in range(3):
        new_pos=[mid_pos[0]+dr[j]*i,mid_pos[1]+dc[j]*i]
        turn.append(new_pos)
# print(turn)
turn=deque(turn)
dr,dc=[0,1,0,-1],[-1,0,1,0]
dir=0

out=0
trun_pos=turn.popleft()
while True:

    if mid_pos ==trun_pos :
        dir=(dir+1)%4
        if turn:
            trun_pos = turn.popleft()

    mid_pos=[mid_pos[0]+dr[dir],mid_pos[1]+dc[dir]]
    if zido[mid_pos[0]][mid_pos[1]]==0 and mid_pos!=[0,0] :continue
    wind(mid_pos,dir)

    if mid_pos==[0,0]:
        break

print(out)