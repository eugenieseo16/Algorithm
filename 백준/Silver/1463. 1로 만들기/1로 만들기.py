import sys

X = int(input())

numbers = [0, 0, 1, 1]
if X <= 3:
    print(numbers[X])
else:
    for num in range(4, X + 1):
        if num % 3 == 0 and num % 2 == 0:
            numbers.append(
                min(numbers[num - 1] + 1, numbers[num // 2] + 1, numbers[num // 3] + 1)
            )
        elif num % 3 == 0:
            numbers.append(min(numbers[num - 1] + 1, numbers[num // 3] + 1))
        elif num % 2 == 0:
            numbers.append(min(numbers[num - 1] + 1, numbers[num // 2] + 1))
        else:
            numbers.append(numbers[num - 1] + 1)
    print(numbers[X])
