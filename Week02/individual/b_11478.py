# 서로 다른 부분 문자열의 개수

import sys
sys.stdin = open('input.txt','r')

word = input()

num = len(word)
result = []

for i in range(num):
    for x in range(i, num):
        result.append(''.join(word[x - i:x + 1]))
result = set(result)

print(len(result))