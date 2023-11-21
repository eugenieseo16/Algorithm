T = int(input())

for t in range(T):
    A, B, X = map(int, input().split())

    ans = A*X - A + B
    print(ans)
