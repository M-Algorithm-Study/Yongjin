# 숨바꼭질 3

import sys
sys.stdin = open('input.txt','r')

from collections import deque

def bfs(s,e):
    q = deque()
    v = [0] * 200001
    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()
        if c == e:
            return v[e] - 1
        for n in (c-1, c+1, c*2):
            if 0 <= n < 200001 and v[n] == 0 :
                if n == c*2:
                    q.appendleft(n) # append만 하면 틀림
                    v[n] = v[c]
                else:                 
                    q.append(n)
                    v[n] = v[c] + 1
    
    return -1


N, K = map(int,input().split())
ans = bfs(N,K)
print(ans)