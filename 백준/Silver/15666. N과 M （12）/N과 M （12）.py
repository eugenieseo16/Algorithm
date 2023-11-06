from collections import defaultdict

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []


def dfs(n):

    if len(ans) == M:
        print(*ans)
        return
    temp = 0
    for i in range(n, N):
        if arr[i] != temp:
            ans.append(arr[i])
            dfs(i)
            temp = ans.pop()


dfs(0)
