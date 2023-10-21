import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

for i in range(1, N):
    if numbers[i-1] + numbers[i] >= numbers[i]:
        numbers[i] = numbers[i-1] + numbers[i]
print(max(numbers))
