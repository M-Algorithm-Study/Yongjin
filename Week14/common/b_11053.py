# 가장 긴 증가하는 부분 수열

import sys
sys.stdin = open('input.txt','r')

N = int(input())
lst = [0] + list(map(int, input().split())) 

# 각 위치에서의 가장 긴 증가하는 부분 수열의 길이를 저장할 리스트를 초기화한다.
dp = [0] * (N + 1)

for i in range(1, N + 1):
    mx = 0
    for j in range(0, i):
        if lst[i] > lst[j]: # 현재 위치의 값이 이전 위치의 값보다 큰 경우
            mx = max(mx, dp[j]) # 현재 위치까지의 가장 긴 부분 수열 길이를 갱신한다.
    dp[i] = mx + 1 # 현재 위치까지의 가장 긴 부분 수열 길이를 저장한다.

print(max(dp))





