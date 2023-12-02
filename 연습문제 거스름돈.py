def solution(n, money):
    money.sort()
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in money:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]
            dp[i] %= 1000000007

    return dp[n]

a=solution(	5, [1, 2, 5])
print(a)