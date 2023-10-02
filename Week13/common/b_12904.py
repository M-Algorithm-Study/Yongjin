# A 와 B

import sys
sys.stdin = open('input.txt','r')

S = input()
T = input()

while len(S) < len(T): # T의 문자열 개수가 S와 같아진다면 멈춘다
    if T[-1] == 'A': # T의 마지막 문자열이 A 이라면
        T = T[:-1] # A를 제외한 나머지 문자열을 T에 저장

    else: # T의 마지막 문자열이 B 이라면
        T = T[:-1][::-1] # 문자열을 뒤집고 B를 제외한 나머지 문자열을 T에 저장한다


if S == T: # S 문자열과 T 문자열이 같으면
    print(1)
else:
    print(0)