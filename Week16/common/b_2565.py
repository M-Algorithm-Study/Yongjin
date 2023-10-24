# 전깃줄

import sys
sys.stdin = open('input.txt','r')

T = int(input())

num = [list(map(int,input().split())) for _ in range(T)]
num.sort() # 시작지점을 기준으로 정렬 [[1, 8], [2, 2], [3, 9], [4, 1], [6, 4], [7, 6], [9, 7], [10, 10]]

dp = [1] * T # dp를 1로 초기화

for i in range(T):
    for j in range(i):
        if num[j][1] < num[i][1]: # [1]번 위치에 숫자가 이전번호의 숫자보다 낮으면 교차
            dp[i] = max(dp[i], dp[j] + 1)

print(T-max(dp))