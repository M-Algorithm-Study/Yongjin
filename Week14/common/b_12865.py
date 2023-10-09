# 평범한 배낭

import sys
sys.stdin = open('input.txt','r')

N, K = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)] # 각 아이템의 무게와 가치를 저장하는 lst

dp = [0] * (K + 1)

for i in range(N):
    w, v = lst[i]  # 각 아이템의 무게와 가치
    for j in range(K, w - 1, -1):  # 무게 제한부터 현재 아이템의 무게까지 역순으로 반복
        if j >= w: # 현재 무게가 아이템의 무게보다 크거나 같을 때
            dp[j] = max(dp[j], dp[j - w] + v) # 현재 무게에서의 최대 가치를 계산하여 저장한다.

print(dp[K])

# 시간 초과
# N, K = map(int,input().split())

# lst = [list(map(int,input().split())) for _ in range(N)]
# dp = [0] * N
# a = []
# b = []
# for i in range(N):
#     for j in range(i):
#         mx = lst[i][0]
#         my = lst[i][1]
#         if i == j:
#             pass
#         else:
#             if mx > K:
#                 pass
#             else:
#                 mx += lst[j][0]
#                 my += lst[j][1]
#                 if mx < K :
#                     continue
#                 elif mx >= K :
#                     a.append((mx,my))
                

# for x,y in a :
#     if K >= x:
#         b.append(y)

# print(max(b))