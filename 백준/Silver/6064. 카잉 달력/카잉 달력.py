import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())


def Kying(M, N, x, y):
    K = x
    while K <= M*N:
        if (K-x) % M == 0 and (K-y) % N == 0:
            return K
        else:
            K += M
    else:
        return -1


for _ in range(T):
    M, N, x, y = map(int, input().split())
    ans = Kying(M, N, x, y)
    print(ans)
