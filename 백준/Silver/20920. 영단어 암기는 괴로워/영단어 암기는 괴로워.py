import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
words = {}
for i in range(N):
    X = sys.stdin.readline().rstrip()
    if len(X) >= M:
        if X in words:
            words[X] += 1
        else:
            words[X] = 1

words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word in words:
    print(word[0])