N = int(input())
P = list(map(int, input().split()))

P.sort()

time = 0
for i in range(N):
    time += P[i] * (N-i)
print(time)