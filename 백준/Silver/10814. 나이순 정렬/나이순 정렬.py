import sys


T = int(input())
names = []
idx = 0
for _ in range(T):
    age, name = sys.stdin.readline().split()
    names.append([int(age), name, idx])
    idx += 1

names.sort(key=lambda x: (x[0], x[2]))
for name in names:
    print(name[0], name[1])
