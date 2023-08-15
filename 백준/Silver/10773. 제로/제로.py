import sys

input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    num = int(input())
    if num != 0:
        numbers.append(num)
    else:
        numbers.pop()
if numbers:
    print(sum(numbers))
else:
    print(0)
