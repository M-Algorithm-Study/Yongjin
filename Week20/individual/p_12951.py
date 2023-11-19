# JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951

import sys
sys.stdin = open('input.txt','r')

def solution(s):
    answer = []
    s = s.split(' ')
    for word in s:
        if word:
            answer.append(word[0].upper() + word[1:].lower())

    return ' '.join(answer)