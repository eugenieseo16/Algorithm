import sys
from collections import defaultdict

door = input()
numbers = defaultdict(int)
for i in range(len(door)):
    numbers[int(door[i])] += 1

temp_num = (numbers[6] + numbers[9])
if temp_num % 2:
    numbers[6] = (temp_num//2) + 1
    numbers[9] = 0

else:
    numbers[6] = (temp_num//2)
    numbers[9] = 0

ans = max(numbers.values())
print(ans)
