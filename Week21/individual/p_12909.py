# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    a = []
    
    for i in s:
        if i == '(':
            a.append(i)
        else:
            if len(a) == 0:
                return False
            else:
                a.pop()
    if len(a) != 0:
        return False

    return True