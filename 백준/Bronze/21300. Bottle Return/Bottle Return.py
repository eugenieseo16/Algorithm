containers = list(map(int, input().split()))
ans = 0    
for contain in containers:
    contain *= 5
    ans += contain
print(ans)