# 아기상어

import sys
sys.stdin = open('input.txt','r')

from collections import deque

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0 # 시작 지점을 0 으로 초기화
            sx, sy = i, j
            break
size = 2
move_num = 0
eat = 0
while True:
    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * n for _ in range(n)] # while문으로 최단거리 도착시 visited 초기화 
    flag = 1e9
    fish = [] # 최단거리이후 fish 초기화
    while q: # bfs
        x, y, count = q.popleft()
        if count > flag: 
            break
        for k in range(4): # 상,하,좌,우 탐색
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: # 범위를 넘어가면 계속 진행
                continue
            if arr[nx][ny] > size or visited[nx][ny]: # arr 이 상어보다 크거나 방문했으면 진행
                continue

            if arr[nx][ny] != 0 and arr[nx][ny] < size: # arr이 0이 아니고 arr이 상어보다 작다면
                fish.append((nx, ny, count + 1)) # 해당 좌표, count fish에 append
                flag = count 
            visited[nx][ny] = True # visited 방문 처리
            q.append((nx, ny, count + 1)) # 해당 좌표, count +1을 q에 append

    if len(fish) > 0:
        fish.sort()
        cnt += 1
        print(fish, cnt)
        print('----------')
        
        x, y, move = fish[0][0], fish[0][1], fish[0][2] # fish의 가장 첫번째를 저장(맨위 왼쪽 맨 끝에 위치한 물고기를 먼저 먹는다는 것은 (세로, 가로) 순서로 오름차순 정렬 하라는 뜻이다.)
        move_num += move
        eat += 1
        arr[x][y] = 0
        if eat == size:
            size += 1
            eat = 0
        sx, sy = x, y
    else:
        break

print(move_num)

# from collections import deque

# N = int(input())

# arr = [list(map(int,input().split())) for _ in range(N)]
# cnt = 0
# pos = []
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 9:
#             pos.append(i)
#             pos.append(j)


# def bfs(s,e):
#     q = deque()
#     visited = [[0]*N for _ in range(N)]
#     visited[s][e] = 1
#     cand = []
#     q.append((s,e))
#     while q:
#         x, y = q.popleft()
#         for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
#             nx , ny = dx + x , dy + y
#             if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
#                 if arr[s][e] > arr[nx][ny] and arr[nx][ny] != 0:
#                     visited[nx][ny] = visited[x][y] + 1
#                     cand.append((visited[nx][ny] - 1, nx, ny))
#                 elif arr[s][e] == arr[nx][ny] :
#                     visited[nx][ny] = visited[x][y] + 1
#                     q.append((nx,ny))
#                 elif arr[nx][ny] == 0:
#                     visited[nx][ny] = visited[x][y] + 1
#                     q.append((nx,ny))
    
#     return sorted(cand, key = lambda x:(x[0], x[1], x[2]))

# i,j = pos
# size = [2,0]
# while 1:
#     arr[i][j] = size[0]
#     cand = deque(bfs(i,j))
    
#     if not cand:
#         break

#     step, nx, ny = cand.popleft()
#     cnt += step
#     size[1] += 1

#     if size[0] == size[1]:
#         size[0] += 1
#         size[1] = 0

#     arr[i][j] = 0
#     i, j = nx, ny

# print(cnt)