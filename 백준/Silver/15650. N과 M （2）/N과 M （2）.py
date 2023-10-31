N, M = map(int, input().split())
queue = []


def dfs(i):
    if len(queue) == M:
        print(*queue)
        return
    for num in range(i, N+1):
        if num not in queue:
            queue.append(num)
            dfs(num+1)
            queue.pop()


dfs(1)
