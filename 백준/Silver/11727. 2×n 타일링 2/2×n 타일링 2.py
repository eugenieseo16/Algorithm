N = int(input())
dp = [0, 1, 3]
if N <= 2:
    pass
else:
    for i in range(3, N + 1):
        dp.append(dp[i - 1] + (dp[i - 2] * 2))

ans = dp[N] % 10007
print(ans)
