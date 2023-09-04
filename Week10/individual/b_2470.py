# 두 용액

import sys
sys.stdin = open('input.txt','r')

N = int(input())

arr = sorted(list(map(int,input().split())))
start , end = 0, N-1
min_sum = float('inf')
A = (0,0)

while start < end:
    sum_ = arr[start] + arr[end]

    if abs(sum_) < min_sum:
        min_sum = abs(sum_)
        A = (arr[start], arr[end])

    if sum_ < 0:
        start += 1
    else:
        end -= 1

print(A[0], A[1])

# while 1:
#     end = start + 1
#     for i in range(end, N):
#         sum_ = arr[start] + arr[end]
#         if sum_ < 0:
#             A.append((arr[start], arr[end], -sum_))
#             end += 1
#         elif sum_ >= 0:
#             A.append((arr[start], arr[end], sum_))
#             end += 1
#     start += 1

#     if start == N:
#         break

# st = sorted(A, key =lambda X: X[2])

# print(st[0][0], st[0][1])
    