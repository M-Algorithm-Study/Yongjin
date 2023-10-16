# 피보나치 수

import sys
sys.stdin = open('input.txt','r')

T = int(input())
a, b = 0, 1 # 초기값 0,1 설정

for i in range(T):
    a, b = b, a+b # a,b 더한 수를 다시 a 저장후 T만큼 반복
    
print(a)