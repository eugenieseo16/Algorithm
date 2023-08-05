import sys

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(list(map(int, sys.stdin.readline().split())))
numbers.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    print(*numbers[i])
