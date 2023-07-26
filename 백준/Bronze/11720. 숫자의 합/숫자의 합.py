N = int(input())
numbers = input()
ans = 0
for i in range(len(numbers)):
    ans += int(numbers[i])
print(ans)