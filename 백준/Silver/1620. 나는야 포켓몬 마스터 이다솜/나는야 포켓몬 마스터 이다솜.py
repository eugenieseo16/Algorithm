import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
monsters = dict()
rev_monsters = dict()

for i in range(1, N + 1):
    monster = input().rstrip()
    monsters[i] = monster
    rev_monsters[monster] = i


for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(monsters[int(question)])
    else:
        print(rev_monsters[question])
