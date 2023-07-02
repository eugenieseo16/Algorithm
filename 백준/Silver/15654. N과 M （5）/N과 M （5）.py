#import sys
#sys.stdin = open('input.txt')

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()



ans = []

def NandM(num):
    if num == M:
        print(" ".join(map(str,ans)))
        return
    for i in range(N):
        if numbers[i] in ans:
            continue
        else:
            ans.append(numbers[i])
            NandM(num+1)
            ans.pop()

NandM(0)