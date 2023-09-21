import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]
dp = [0] * N

if N <= 2:
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max((stairs[2] + stairs[1]), (stairs[2] + stairs[0]))
    for i in range(3, N):
        dp[i] = max((dp[i - 3] + stairs[i - 1] + stairs[i]), (dp[i - 2] + stairs[i]))
    print(dp[N - 1])
