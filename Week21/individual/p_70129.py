# 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = []
    a = 0
    cnt = 0
    
    while 1:
        if s == '1':
            break
        
        a += s.count('0')
        s = s.replace('0','')
        s = bin(len(s))[2:]
        cnt += 1
    
    answer = [cnt,a]
    return answer