N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
ans = []


def dfs(n):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(n, N):
        ans.append(numbers[i])
        dfs(i)
        ans.pop()


dfs(0)