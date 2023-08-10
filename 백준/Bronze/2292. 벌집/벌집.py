N = int(input())
count = 1
start = 1
while start < N:
    start += count * 6
    count += 1
print(count)
