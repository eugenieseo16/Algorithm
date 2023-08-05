import sys

T = int(input())

def VPS(PS):
    stack = []
    for i in PS:
        if i == "(":
            stack.append("(")
        elif i == ")" and len(stack) == 0:
            return "NO"
        elif i == ")":
            stack.pop()
    if stack:
        return "NO"
    else:
        return "YES"


for _ in range(T):
    PS = sys.stdin.readline()
    print(VPS(PS))
