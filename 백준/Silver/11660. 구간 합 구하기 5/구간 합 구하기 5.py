import sys

N, M = map(int, sys.stdin.readline().split())
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(numbers) [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
acc_sum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        acc_sum[i][j] = (
            numbers[i - 1][j - 1]
            + acc_sum[i - 1][j]
            + acc_sum[i][j - 1]
            - acc_sum[i - 1][j - 1]
        )

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans = (
        acc_sum[x2][y2]
        - acc_sum[x1 - 1][y2]
        - acc_sum[x2][y1 - 1]
        + acc_sum[x1 - 1][y1 - 1]
    )
    print(ans)