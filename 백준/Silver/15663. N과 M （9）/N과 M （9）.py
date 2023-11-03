N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visitied = list([0] * N)
res = []


def dfs():

    if len(res) == M:
        print(*res)
        return

    prev = 0
    for i in range(N):
        if not visitied[i] and prev != numbers[i]:
            res.append(numbers[i])
            visitied[i] = 1
            prev = numbers[i]
            dfs()
            visitied[i] = 0
            res.pop()


dfs()
