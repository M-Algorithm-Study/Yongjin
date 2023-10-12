# 피보나치 수

import sys
sys.stdin = open('input.txt','r')

T = int(input())
a, b = 0, 1

for i in range(T):
    a, b = b, a+b

print(a)