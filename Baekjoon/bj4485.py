# 녹색 옷 입은 애가 젤다지?

def bfs(hp, r, c):
    global visited
    if r == n - 1 and c == n - 1:
        return hp
    ans=9*n*n+1
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    for i in range(4):
        new_r = r + dr[i]
        new_c = c + dc[i]
        if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n: continue
        if visited[new_r][new_c] <= hp+zido[new_r][new_c] : continue

        visited[new_r][new_c]=hp+zido[new_r][new_c]
        ans=min(ans,bfs(hp+zido[new_r][new_c],new_r,new_c))
    return ans


cnt=0
while True:
    cnt+=1
    n = int(input())
    if n == 0: break
    visited = []
    hp = 0
    zido = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        zido.append(temp)
    visited = [[n*n*9+1 for _ in range(n)] for _ in range(n)]
    visited[0][0] = zido[0][0]
    print("Problem "+str(cnt)+": "+str(bfs(zido[0][0], 0, 0)))

