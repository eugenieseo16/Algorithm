import sys
input = sys.stdin.readline

T = int(input())

def checking(num_pos, num_neg):
    if num_pos > num_neg:
        print("YES")
    else:
        print("NO")


for _ in range(T):
    len_num = int(input())
    numbers = list(map(int, input().split()))
    prev_sum = 0
    num_pos = 0
    num_neg = 0

    for idx in range(len_num):
        num = numbers[idx]
        # 1. 만약 누적합이 양수
        if prev_sum > 0:
            # 새로운 수가 양수
            if num > 0:
                prev_sum = num
                num_pos += 1
            #  새로운 수가 음수
            elif num < 0:
                # 누적합이 양수
                if prev_sum + num > 0:
                    prev_sum += num
                # 누적합이 음수
                else:
                    prev_sum = num
                    num_pos += 1
        # 2. 누적합이 음수
        elif prev_sum < 0:
            # 새로운 수가 양수
            if num > 0:
                # 누적합이 양수
                if prev_sum + num > 0:
                    prev_sum += num
                else:
                    prev_sum = num
                    num_neg += 1
            # 새로운 수가 음수
            elif num < 0:
                prev_sum += num
        else:
            prev_sum = num
    # 마지막 수 계산
    else:
        if prev_sum > 0:
            num_pos += 1
        elif prev_sum < 0:
            num_neg += 1
    
    # 결과 반환      
    checking(num_pos, num_neg)
