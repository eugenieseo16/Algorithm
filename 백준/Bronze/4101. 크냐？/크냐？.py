A,B = map(int,input().split())
while A != 0 and B != 0:
    if A > B:
        print('Yes')
    else:
        print('No')
    A,B = map(int,input().split())