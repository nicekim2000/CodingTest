def solution(sales, links):
    n = len(sales)
    tree = [[] for _ in range(n + 1)]
    dp = [[0, 0] for _ in range(n + 1)]

    # 트리 구조 생성
    for a, b in links:
        tree[a].append(b)

    # 재귀 함수로 각 노드 계산
    def dfs(node):
        dp[node][0] = 0
        dp[node][1] = sales[node - 1]

        if not tree[node]:
            return

        extra_cost = float('inf')

        for child in tree[node]:
            dfs(child)
            # 자식이 워크숍에 참여하지 않을 때 손실이 참여할때 보다 클때
            if dp[child][0] < dp[child][1]:
                dp[node][0] += dp[child][0]
                dp[node][1] += dp[child][0]
                extra_cost = min(extra_cost, dp[child][1] - dp[child][0])
            else:
                dp[node][0] += dp[child][1]
                dp[node][1] += dp[child][1]
                extra_cost = 0

        dp[node][0] += extra_cost

    dfs(1)
    print(1)
    return min(dp[1])

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]])) # 44