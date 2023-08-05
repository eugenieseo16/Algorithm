import sys

N = int(input())
stack = []

def program(command):
    if command[:4] == "push":
        stack.append(int(command[5:]))
    elif command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)


for _ in range(N):
    command = sys.stdin.readline().rstrip()
    program(command)
