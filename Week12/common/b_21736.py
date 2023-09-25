# 헌내기는 친구가 필요해

import sys
sys.stdin = open('input.txt','r')

from collections import deque

def bfs(si,sj):
    global cnt
    q = deque()
    visited[si][sj] = 1
    q.append((si,sj))
    cnt = 0
    while q:
        x,y = q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)): # 범위 탐색
            nx, ny = x + dx , y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 : # 범위 확인
                if arr[nx][ny] == 'O': # 빈공간이라면
                    visited[nx][ny] = 1 # 방문처리
                    q.append((nx,ny)) # q에 좌표 저장

                elif arr[nx][ny] == 'X': # 벽이라면 패스
                    pass

                elif arr[nx][ny] == 'P': # 사람을 찾으면
                    visited[nx][ny] = 1 # 방문처리
                    q.append((nx,ny)) # q에 좌표저장
                    cnt += 1 # 카운트


N, M = map(int,input().split()) 
arr = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]


for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I' : # 도연이 위치 찾기
            bfs(i,j)


if cnt == 0:
    print('TT')
else:
    print(cnt)