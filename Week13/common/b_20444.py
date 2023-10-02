# 색종이와 가위

import sys
sys.stdin = open('input.txt','r')

n, k = map(int, input().split())
left, right = 0 , n # 이진탐색 왼쪽 오른쪽을 0과 n으로 초기화
isPossible = False

while left <= right:
    rowCut = (left + right) // 2 # 가로 
    colCut = n - rowCut # 세로
    pieces = (rowCut + 1) * (colCut + 1) # 가로, 세로 각각 rowCut, colCut번씩 잘랐다면 (rowCut + 1) * (colCut + 1) 조각이 생김
    if k == pieces:
        print('YES')
        isPossible = True
        break
    if k > pieces: # K 값 보다 조각수가 작다면
        left = rowCut + 1 # 왼쪽값을 가로 + 1 값으로 저장 (왼쪽에서 오른쪽으로 이동)
    else:
        right = rowCut - 1 # 오른쪽값을 가로 - 1 값으로 저장 (오른쪽에서 왼쪽으로 이동)

if isPossible == False:
    print('NO')