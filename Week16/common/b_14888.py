# 연산자 끼워넣기

import sys
sys.stdin = open('input.txt','r')

def dfs(n, sm, add , sub , mul, div):
    global mx, mn
    if int(1e9) < sm or int(-1e9) > sm : # 주어진 범위를 넘어가면 종료
        return

    if n == N: # n이 증가해서 N과 같아지면 종료
        mx = max(mx, sm)
        mn = min(mn, sm)
        return
    
    if add > 0:
        dfs(n+1, sm + lst[n], add - 1 , sub , mul, div)
    if sub > 0:
        dfs(n+1, sm - lst[n], add , sub - 1 , mul, div)
    if mul > 0:
        dfs(n+1, sm * lst[n], add , sub , mul - 1, div)
    if div > 0:
        dfs(n+1, int(sm / lst[n]), add , sub , mul, div - 1)

        
N = int(input())
lst = list(map(int,input().split()))
add , sub , mul, div = map(int,input().split())

mx , mn = int(-1e9), int(1e9) # mx, mn 초기화
dfs(1, lst[0], add , sub , mul, div)
print(mx)
print(mn)
