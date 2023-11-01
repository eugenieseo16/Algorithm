N, M = map(int, input().split())

numbers = []


def dfs(n):
    if len(numbers) == M:
        print(*numbers)
        return
    for i in range(n, N+1):
        numbers.append(i)
        dfs(i)
        numbers.pop()


dfs(1)
