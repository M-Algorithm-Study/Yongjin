# 최고의 집합
# https://school.programmers.co.kr/learn/courses/30/lessons/12938


def solution(n, s):
    
    if n > s:
        return [-1]
    
    div = s // n
    remain = s % n
    
    answer = [div] * n
    
    for i in range(remain):
        answer[i] = answer[i] + 1
    
    answer.sort()
    return answer



# 시간초과
# from itertools import combinations_with_replacement

# def solution(n, s):
#     combinations = combinations_with_replacement(range(1, s + 1), n)
#     lst = [comb for comb in combinations if sum(comb) == s]
#     answer = []
    
#     if not lst:
#         return [-1]
    
#     for i in lst:
#         arr = 1
#         for j in i:
#             arr *= j
#         answer.append([arr,list(i)])
    
#     max_answer = max(answer, key=lambda x: x[0])
#     result = max_answer[1]
    
#     return result