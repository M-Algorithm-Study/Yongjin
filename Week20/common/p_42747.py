# H-index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort()
    
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i:
            return len(citations) - i
    return 0

citations = [3, 0, 6, 1, 5]

print(solution(citations))
#    citations	  return
# [3, 0, 6, 1, 5]	3