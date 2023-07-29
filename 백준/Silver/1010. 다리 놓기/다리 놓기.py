import sys

TC = int(input())
for t in range(TC):
    west, east = map(int, sys.stdin.readline().split())

    num1 = 1
    num2 = 1
    for w in range(west):
        num1 *= east - w
        num2 *= w + 1
    print(num1 // num2)
