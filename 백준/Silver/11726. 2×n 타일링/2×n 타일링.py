N = int(input())

way = [0, 1, 2, 3]

if N <= 3:
    print(way[N])
else:
    for i in range(4, N + 1):
        way.append(way[i - 2] + way[i - 1])
    print(way[N] % 10007)
