L, P = map(int, input().split())
ppl = L * P
numbers = list(map(int, input().split()))
ans = []
for num in numbers:
    ans.append(num - ppl)
print(*ans)