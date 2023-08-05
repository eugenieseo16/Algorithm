import sys
from collections import deque

N = int(input())
Q = deque()

def program(command):
    if command[0] == "push_front":
        Q.appendleft(int(command[1]))
    elif command[0] == "push_back":
        Q.append(int(command[1]))
    elif command[0] == "pop_front":
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if Q:
            print(Q.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(Q))
    elif command[0] == "empty":
        if Q:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif command[0] == "back":
        if Q:
            print(Q[-1])
        else:
            print(-1)


for _ in range(N):
    command = sys.stdin.readline().split()
    program(command)
