import sys

#sys.stdin = open("input.txt")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    num = int(input())
    num_list = [[1, 0], [0, 1]]
    if num < 2:
        print(*num_list[num])
    else:
        for i in range(2, num + 1):
            x = num_list[i - 2][0] + num_list[i - 2][1]
            y = num_list[i - 1][0] + num_list[i - 1][1]
            num_list.append([x, y])
        print(*num_list[num])
