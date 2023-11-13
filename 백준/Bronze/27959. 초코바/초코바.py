money, choco = map(int, input().split())

money *= 100
if money - choco >= 0:
    print("Yes")
else:
    print("No")