numbers = list(input().split("-"))
length = len(numbers)
for i in range(length):
    if "+" in numbers[i]:
        numbers[i] = sum(map(int, numbers[i].split("+")))
if length == 1:
    print(int(numbers[0]))
else:
    ans = int(numbers[0])
    for i in range(1, length):
        ans -= int(numbers[i])
    print(ans)