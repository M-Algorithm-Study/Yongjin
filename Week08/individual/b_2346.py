# 풍선 터뜨리기

import sys
sys.stdin = open('input.txt','r')
from collections import deque

T = int(input())
dq = deque(enumerate(map(int,input().split())))
a = []

while dq:
    idx, paper = dq.popleft()
    a.append(idx + 1)

    if paper > 0:
        dq.rotate(-(paper - 1))
    elif paper < 0:
        dq.rotate(-paper)
print(' '.join(map(str,a)))