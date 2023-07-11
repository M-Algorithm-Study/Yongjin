# 쇠막대기

import sys
sys.stdin = open('input.txt', 'r')

T = list(input())
count = 0  
open_count = 0  

for i in range(len(T)):
    if T[i] == '(': # T가 ( 일면
        open_count += 1 # 막대기 생성
    else: # ) 일때
        open_count -= 1  # 막대기 여기까지
        if T[i-1] == '(':  # () 를 완성하고 T의 이전 값이 ( 이면 
            count += open_count # 레이저로 막대기를 잘랐을때 막대기의 갯수를 더한다
        else:
            count += 1 # 만약 이전 값이 ) 이라면 하나의 막대기의 끝 이므로 이후 막대기 개수인 1을 더해 준다.

print(count)