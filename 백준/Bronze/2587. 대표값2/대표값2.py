import sys

input = sys.stdin.readline
numbers = []
ans = 0
for _ in range(5):
    x = int(input())
    numbers.append(x)
    ans += x
numbers.sort()
print(ans // 5)
print(numbers[2])
