import sys
input = sys.stdin.readline
S = set()


def cal(S, word, num):
    if word == "add":
        S.add(num)

    elif word == "remove":
        S.discard(num)

    elif word == "check":
        if num in S:
            print(1)
        else:
            print(0)

    elif word == "toggle":
        if num in S:
            S.discard(num)
        else:
            S.add(num)

    elif word == "all":
        S = set(i for i in range(1, 21))

    elif word == "empty":
        S = set()


N = int(input())
for j in range(N):
    words = input().split()
    if len(words) == 2:
        word = words[0]
        num = int(words[1])
        cal(S, word, num)

    else:
        word = words[0]
        if word == "all":
            S = set(i for i in range(1, 21))
        elif word == "empty":
            S = set()