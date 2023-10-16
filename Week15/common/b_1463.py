# 1로 만들기

import sys
sys.stdin = open('input.txt','r')

T = int(input())
# dp 배열 초기화: T까지의 최소 연산 횟수를 저장하기 위한 배열
dp = [0] * (T+1)

for i in range(2, T+1):
    # 1을 더하는 경우 (1을 빼는 경우)
    dp[i] = dp[i-1] + 1
    
    # 현재 수가 2로 나누어 떨어지면
    if i % 2 == 0:
        # 현재까지의 최소 연산 횟수와 2로 나눈 수의 최소 연산 횟수 중 최솟값 선택
        dp[i] = min(dp[i], dp[i//2] + 1)
    
    # 현재 수가 3으로 나누어 떨어지면
    if i % 3 == 0:
        # 현재까지의 최소 연산 횟수와 3으로 나눈 수의 최소 연산 횟수 중 최솟값 선택
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[T])