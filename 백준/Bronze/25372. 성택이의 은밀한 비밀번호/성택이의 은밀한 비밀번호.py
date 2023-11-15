N = int(input())

for _ in range(N):
    pwd = len(input())
    if pwd <= 9 and 6 <= pwd:
        print("yes") 
    else:
        print("no")