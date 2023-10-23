A, B = map(int, input().split())
cnt = 1
while B > A:
    if str(B)[-1] == '1':
        B = str(B)[:-1]
        B = int(B)
        cnt += 1

    elif B % 2 == 0:
        B = B//2
        cnt += 1
    else:
        break
if A == B:
    print(cnt)
else:
    print(-1)
