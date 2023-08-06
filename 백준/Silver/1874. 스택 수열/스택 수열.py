import sys

stack = []
count = 1
is_possible = True
answer = []
N = int(input())

for i in range(1, N + 1):
    num = int(input())
    while count <= num:
        stack.append(count)
        count += 1
        answer.append("+")
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        is_possible = False
        break
if is_possible:
    for ans in answer:
        print(ans)
else:
    print("NO")
