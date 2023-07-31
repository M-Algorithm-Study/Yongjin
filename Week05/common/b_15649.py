# N 과 M

import sys
sys.stdin = open('input.txt', 'r')

def dfs(n,lst):
    if M == n: # M 과 n 이 같으면 종료
        ans.append(lst)
        return 
    for i in range(1, N+1):
        if visited[i] == 0: # 방문 하지 않았다면
            visited[i] = 1 # 방문 처리
            dfs(n+1 , lst+[i]) # n+1, 해당 숫자를 리스트에 추가 
            visited[i] = 0 # 다시 초기화


N, M = map(int,input().split())
ans = []
visited = [0] * (N+1)

dfs(0, [])

for lst in ans:
    print(*lst)