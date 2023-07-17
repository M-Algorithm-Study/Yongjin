# 구간 합 구하기 4

import sys
sys.stdin = open('input.txt','r')

N, M = map(int,input().split())

num = list(map(int, input().split()))
sum_1 = 0
arr = [0]

for i in range(N):
    sum_1 += num[i]
    arr.append(sum_1)

for i in range(M):
    a,b = map(int,input().split())
    print(arr[b]-arr[a-1])