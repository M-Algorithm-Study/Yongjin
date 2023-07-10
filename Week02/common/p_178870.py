# 연속된 부분 수열의 합
# 시간초과 발생한 코드....

sequence = [2, 2, 2, 2, 2]
k = 6
def solution(sequence, k):
    answer = []
    b = []
    result = []
    cnt = [100]
    cnt_1 = [1]
    for i in range(len(sequence)):
        for x in range(i, len(sequence)):
            idxs = [i,x]
            sublist_sum = sum(sequence[i:x+1])
            if sublist_sum == k:
                answer.append(idxs)
                break
            elif sublist_sum > k:
                break
    
    for start, end in answer:
        result = end - start
        if cnt[0] > result:
            cnt.pop()
            cnt.append(result)
            cnt_1.pop()
            cnt_1.append([start,end])

    for i in cnt_1:
        return i

solution(sequence, k)