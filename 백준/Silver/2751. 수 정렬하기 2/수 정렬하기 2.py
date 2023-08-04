import sys

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()
for i in range(N):
    print(numbers[i])
