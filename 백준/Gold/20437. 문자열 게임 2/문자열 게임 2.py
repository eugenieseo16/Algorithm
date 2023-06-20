

from collections import defaultdict
# defaultdict : 키의 존재 여부를 확인하지 않고 바로 값을 증가시키거나 처리해야 하는 경우 사용

def string_game(W, K):
    if K == 1:
        return [1, 1]
    words = defaultdict(int)
    interval = []
    length = len(W)

    # 해당 알파벳의 value 값을 += 1
    for word in W:
        words[word] += 1
    for key, value in words.items():
        #  알파벳의 갯수가 K개 이상이라면
        if value >= K:
            # key값의 인덱스를 리스트에 기록
            index_list = list(filter(lambda x : W[x] == key, range(length)))
            # K개 일때의 길이를 세야 하니까 K 단위로 끊어서 길이 기록
            for i in range(len(index_list)-K+1):
                interval.append(index_list[i+K-1] - index_list[i])

    if not interval:
        return -1
    else:
        return min(interval)+1, max(interval)+1



T = int(input())
for tc in range(T):
    W = input()
    K = int(input())
    
    result = string_game(W, K)
    if result == -1:
        print(-1)
    else:
        print(*result)
