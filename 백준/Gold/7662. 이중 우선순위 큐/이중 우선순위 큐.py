import sys
import heapq

# sys.stdin = open("input.txt")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    min_heap, max_heap = [], []
    visited = dict()
    k = int(input())
    for i in range(k):
        command, num = input().split()
        num = int(num)
        # 삽입 연산인 경우
        if command[0] == "I":
            # 이미 존재하는 숫자라면
            if num in visited:
                # 방문 횟수 증가
                visited[num] += 1
                # 최소,최대 힙에 삽입
            else:
                # 없는 숫자면 방문 기록
                visited[num] = 1
            # 최소,최대 힙에 삽입
            heapq.heappush(min_heap, num)
            # 최대 힙에는 부호를 바꿔서 삽입
            heapq.heappush(max_heap, -num)
        else:
            # 최댓값 삭제 연산인 경우
            if num == 1:
                while max_heap and visited[-max_heap[0]] <= 0:
                    # 방문횟수가 0 이하인 경우 삭제
                    heapq.heappop(max_heap)
                # 최대 힙이 비어있지 않다면
                if max_heap:
                    # 방문 횟수 감소
                    visited[-max_heap[0]] -= 1
                    # 최대 힙에서 삭제
                    heapq.heappop(max_heap)
            # 최솟값 삭제 연산인 경우
            else:
                while min_heap and visited[min_heap[0]] <= 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0]] -= 1
                    heapq.heappop(min_heap)
            # 모든 연사 이후 유효하지 않은 원소를 힙에서 제거
            while min_heap and visited[min_heap[0]] <= 0:
                heapq.heappop(min_heap)
            while max_heap and visited[-max_heap[0]] <= 0:
                heapq.heappop(max_heap)
    if max_heap and min_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")
