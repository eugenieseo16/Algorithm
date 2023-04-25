
def sugar(num):
    count = 0
    left = 0
    max_5 = num // 5


    for i in range(max_5, -1, -1):
        left = num - i*5
        count += i

        if left == 0:
            return count
        else:
            count += left // 3
            left = left % 3
            if left == 0:
                return count
            else:
                count = 0
                left = 0
    else:
        return -1


N = int(input())
print(sugar(N))