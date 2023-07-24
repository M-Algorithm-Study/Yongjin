# 영단어 암기는 괴로워

import sys
sys.stdin = open('input.txt','r')

N, M = map(int,input().split())
dik = dict()

for i in range(N):
    word = input()
    if word in dik:
        if len(word) < M:
            pass
        else:
            dik[word] += 1
    else:
        if len(word) < M:
            pass
        else:
            dik[word] = 1


sorted_items = sorted(dik.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

# -x[1] : 각 항목의 두번째 요소를 기준으로 항목을 정렬 / -는 값을 내림차순으로 정렬하는 데 사용
# -len(x[0]) : 사전에서 키(단어) 각 항목의 첫 번째 요소의 길이를 기준으로 항목을 정렬
# x[0] : 항목의 첫 번째 요소를 기준으로 항목을 알파벳순으로 정렬

for key, value in sorted_items:
    print(key)
    