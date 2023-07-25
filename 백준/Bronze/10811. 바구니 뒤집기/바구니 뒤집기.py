N, M = map(int, input().split())
numbers = [i for i in range(1, N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr = numbers[a - 1 : b]
    arr.reverse()
    numbers[a - 1 : b] = arr

print(*numbers)
