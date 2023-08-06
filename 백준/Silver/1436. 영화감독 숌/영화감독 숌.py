N = int(input())
count = 0
num = 666
while True:
    if "666" in str(num):
        count += 1
    if count == N:
        break
    num += 1
print(num)
