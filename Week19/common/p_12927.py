# 야근 지수
# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq

def solution(n, works):
    answer = 0
    lst = []
    N = sum(works) - n
    if N <= 0:
        return 0

    for i in works:
        heapq.heappush(lst,-i)
        
    for _ in range(n):
        i = heapq.heappop(lst)
        i = i + 1
        heapq.heappush(lst, i)
    
    for i in lst:
        answer += i**2
        
    return answer