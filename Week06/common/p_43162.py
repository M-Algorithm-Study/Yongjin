# 네트워크

def dfs(x, computers, visited):
    visited[x] = True # 방문 표시
    for a,b in enumerate(computers[x]):
        if b == 1 and (not visited[a]): # item이 1 이고 visited 순서에 방문하지 않았다면
            dfs(a, computers, visited) # dfs 동작
            
def solution(n, computers):
    visited = [False] * n 
    cnt = 0
    
    for i in range(n):
        if not visited[i]: # 방문하지 않았으면
            dfs(i,computers, visited) # dfs 동작
            cnt += 1 # cnt + 1
    return cnt

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n,computers))