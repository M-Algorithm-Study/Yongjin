# N-Queen

import sys
sys.stdin = open('input.txt','r')

N = int(input())

def dfs(n):
    global ans
    if n == N: # 종료 조건 N행까지 진행한 경우 성공
        ans += 1
        return
    
    for j in range(N): 
        if v1[j] == v2[n+j] == v3[n-j] == 0: # 열 대각선이 모두 0 인경우(Q가 없는 경우)
            v1[j] = v2[n+j] = v3[n-j] = 1 # 열 대각선 모두 1로 바꿈
            dfs(n+1) # n을 1씩 증가해서 dfs반복
            v1[j] = v2[n+j] = v3[n-j] = 0 # 증가이후 0으로 변경

ans = 0
v1 = [0] * N # 열
v2 = [0] * (2*N) # 대각선
v3 = [0] * (2*N) 
dfs (0)
print(ans)