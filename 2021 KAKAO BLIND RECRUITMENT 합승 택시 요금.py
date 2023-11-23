def solution(n, s, a, b, fares):
    def floyd_warshall(graph):
        n = len(graph)

        # 초기 거리는 주어진 그래프를 그대로 사용
        dist = [row[:] for row in graph]

        # k를 거치는 모든 정점 쌍 (i, j)에 대해 최단 거리 갱신
        for k in range(1,n):
            for i in range(1,n):
                for j in range(1,n):
                    if i==j : dist[i][j]=0
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist

    answer = 0
    graph = [[1e9 for _ in range(n + 1)] for _ in range(n + 1)]
    for f in fares:
        graph[f[0]][f[1]] = f[2]
        graph[f[1]][f[0]] = f[2]

    paths = floyd_warshall(graph)
    for i in range(1,len(paths)):
        print(paths[i][1:])
    min_value=1e9
    for i in range(1,n+1):
        temp=paths[s][i]+paths[i][a]+paths[i][b]
        min_value=min(min_value,temp)


    return min_value

a=solution(	6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
print(a)