import sys
from collections import deque

N = int(input())
Q = deque()


def program(command):
    if command[:4] == "push":
        Q.append(int(command[5:]))
    elif command == "front":
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif command == "back":
        if Q:
            print(Q[-1])
        else:
            print(-1)
    elif command == "size":
        print(len(Q))
    elif command == "empty":
        if Q:
            print(0)
        else:
            print(1)
    elif command == "pop":
        if Q:
            print(Q.popleft())
        else:
            print(-1)


for _ in range(N):
    command = sys.stdin.readline().rstrip()
    program(command)
