# 토마토

import sys
sys.stdin = open('input.txt','r')

from collections import deque

def bfs():
    q = deque()
    v = [[[0] * M for _ in range(N)] for _ in range(H)] # 빈 리스트 생성

    cnt = 0
    for h in range(H): # for문으로 리스트 전체 순회
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1 : # 토마토가 존재 하면 
                    q.append((h,i,j)) # 해당 좌표 덱에 append
                    v[h][i][j] = 1 # 방문 리스트에도 1 바꾸기
                elif arr[h][i][j] == 0 : # 토마토가 존재 하지 않으면
                    cnt += 1 # 1씩 더해주기
    
    while q : # q가 존재한다면
        ch, ci, cj = q.popleft() # q의 좌표를 각각 저장

        for dh, di, dj in ((0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1), (-1, 0, 0), (1, 0, 0)): # 위 아래 상 하 좌 우 좌표
            nh, ni, nj = ch+dh, ci+di, cj+dj # 저장된 q의 좌표값에 위 아래 상 하 좌 우 좌표를 더해 좌표 탐색
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and v[nh][ni][nj] == 0 and arr[nh][ni][nj] == 0: # 만약 범위내에 그리고  탐색한 좌표와 방문좌표 그리고 arr이 0 이라면
                q.append((nh,ni,nj)) # 덱에 더한 좌표를 저장
                v[nh][ni][nj] = v[ch][ci][cj] + 1  # 방문 좌표에 원래좌표 +1 값을 더해준다
                cnt -= 1 # 안익은 토마토 1개 익음

    if cnt == 0: # 모든 토마토 익었으면
        return v[ch][ci][cj] - 1 # 방문좌표 값에 -1을 해준다
    else: # 아니라면
        return -1 # -1 출력

M,N,H = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)] # 리스트 생성
ans = bfs()
print(ans)