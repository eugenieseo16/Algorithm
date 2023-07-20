N = int(input())
numbers = list(map(int, input().split()))
stack = []
ans = []

for i in range(N):
    while stack and stack[-1][1] < numbers[i]:
        stack.pop()

    if not stack:
        ans.append(0)
    else:
        ans.append(stack[-1][0] + 1)

    stack.append((i, numbers[i]))

print(*ans)
