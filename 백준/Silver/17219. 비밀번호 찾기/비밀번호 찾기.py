import sys

input = sys.stdin.readline

N, M = map(int, input().split())
passwords = dict()
for _ in range(N):
    address, password = input().split()
    passwords[address] = password

for _ in range(M):
    ans_key = input().rstrip()
    print(passwords[ans_key])
