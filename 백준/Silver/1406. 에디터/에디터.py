import sys
from collections import deque

input = sys.stdin.readline

words = deque(input().rstrip())
after_cursor = deque()
n = int(input())
for i in range(n):
    command = input().split()
    # 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
    if command[0] == "L":
        if words:
            after_cursor.appendleft(words.pop())

    # 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
    elif command[0] == "D":
        if after_cursor:
            words.append(after_cursor.popleft())

    # 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
    elif command[0] == "B":
        if words:
            words.pop()

    # $라는 문자를 커서 왼쪽에 추가함
    else:
        words.append(command[1])

ans = words + after_cursor
ans = "".join(list(ans))
print(ans)
