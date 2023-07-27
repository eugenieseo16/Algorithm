N = int(input())
for n in range(N):
    num, string = input().split()
    ans = ""
    for s in string:
        ans += int(num) *s
    print(ans)    
    