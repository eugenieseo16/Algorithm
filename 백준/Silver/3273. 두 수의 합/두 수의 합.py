

N = int(input())
numbers =  list(map(int, input().split()))
X = int(input())

numbers = sorted(numbers)

end = N - 1
answer = 0
for start in range(N-1):
    while start < end:
        temp_sum = numbers[start] + numbers[end]
        if temp_sum == X:
            answer += 1
            end -= 1
        elif temp_sum > X :
            end -= 1
        else:
            break
print(answer)
