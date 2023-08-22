import sys

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))

numbers.sort()
for i in range(N):
    print(numbers[i])
