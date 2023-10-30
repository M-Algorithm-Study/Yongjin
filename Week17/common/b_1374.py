# 강의실

import sys, heapq
sys.stdin = open('input.txt','r')

T = int(input())
arr = [list(map(int,input().split())) for _ in range(T)]
arr = sorted(arr, key =lambda x: x[1])

min_heap = []
count = 0

#다른 수업 시간과 겹치지 않으면 이전 수업 pop
for i in arr:
    while min_heap and min_heap[0]<=i[1]: #가장 일찍 끝나는 수업보다 늦게 시작하면(겹치지 않으면)
        heapq.heappop(min_heap) #heap에서 가장 작은 원소 내보냄
    heapq.heappush(min_heap, i[2]) #i 수업의 끝나는 시간 힙에 추가
    count = max(count, len(min_heap))

print(count)


# arr 순서
# [3, 2, 14]
# [1, 3, 8]
# [8, 6, 27]
# [5, 6, 20]
# [2, 7, 13]
# [4, 12, 18]
# [6, 15, 21]
# [7, 20, 25]