num = int(input())

for i in range(1, num + 1):
    ans = " " * ((num * 2 - ((i * 2) - 1)) // 2)
    ans += "*" * ((i * 2) - 1)
    print(ans)
for j in range(num - 1, 0, -1):
    star = " " * ((num * 2 - ((j * 2) - 1)) // 2)
    star += "*" * ((j * 2) - 1)
    print(star)