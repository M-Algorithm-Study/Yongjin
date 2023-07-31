# 암호 만들기

import sys
sys.stdin = open('input.txt','r')

def dfs(n, rst, last_num):
    global lst
    if n == N: # n 과 M이 같으면 종료
        cnt_1 = 0 # 모음 카운트
        cnt_2 = 0 # 자음 카운트
        for i in rst:
            if  'a' in lst[i] or 'e' in lst[i] or 'i' in lst[i] or 'o' in lst[i] or 'u' in lst[i]: # 만약 모음이 리스트 안에 있다면
                cnt_1 += 1 # cnt_1 카운트
            else:
                cnt_2 += 1 # 자음이라면 cnt_2 카운트

        if cnt_1 >= 1 and cnt_2 >=2: # 모음 최소 1개이상 자음 최소 2개이상 일때
            result.append(rst) # rst값을 result로 append
            cnt_1 = 0 # 모음 카운트 초기화
            cnt_2 = 0 # 자음 카운트 초기화
        return 
    for i in range(M):
        if visited[i] == 0 and i > last_num: # 방문하지 않았고 이전 인덱스보다 큰 경우에만
            visited[i] = 1 # 방문처리
            dfs(n+1, rst+[i], i) # n+1, rst에 i 값을 더한다, last_num 비교를 위한 지금 인덱스
            visited[i] = 0 # 방문 초기화

N, M = map(int,input().split())
lst = sorted(list(map(str,input().split()))) # 문자를 사전으로 정렬
result = []
visited = [0] * (M)

dfs(0, [], -1)
cnt = 0

for i in result:
    for j in i:
        print(lst[j], end='')
    print()

