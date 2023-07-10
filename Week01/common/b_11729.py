# 하노이 탑 이동 순서

import sys
sys.stdin = open('input.txt','r')

def hanoi(num, one, two, three): # 원판개수, 시작기둥, 대상기둥, 보조기둥
    if num == 1:
        print(one, two) # 시작기둥 => 대상기둥
    else:
        hanoi(num-1, one, three, two) # 원판개수 -1, 시작기둥, 보조기둥, 대상기둥
        print(one, two) # 시작기둥 => 대상기둥
        hanoi(num-1, three, two, one) # 원판개수 -1, 보조기둥, 대상기둥, 시작기둥



num = int(input())
print((2 ** num) -1)
hanoi(num, 1,3,2)