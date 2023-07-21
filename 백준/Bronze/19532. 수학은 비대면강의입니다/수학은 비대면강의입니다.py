x1, y1, c1, x2, y2, c2 = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (x1 * i) + (y1 * j) == c1 and (x2 * i) + (y2 * j) == c2:
            print(i, j)
