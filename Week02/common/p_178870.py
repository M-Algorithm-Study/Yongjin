# 연속된 부분 수열의 합
# 시간초과 발생한 코드....

sequence = [1, 1, 1, 2, 3, 4, 5]
k = 5
def solution(sequence, k):
    answer = []
    result = 0
    start = 0
    sublist_sum = 0 # 누적합
    min_length = float('inf') #양의 무한대
    length = 0 # 인덱스 차
    for end in range(len(sequence)):
        sublist_sum += sequence[end]
        
        while sublist_sum > k: # 누적합이 k를 초과하면
            sublist_sum -= sequence[start] # 누적합에서 빼주기
            start += 1 # start값을 증가시켜 누적합 차를 통해 sublist_sum 조건을 맞춘다
        
        if sublist_sum == k: # start 부터 end까지 합과 k가 같아지면
            answer.append((start, end)) # start, end (인덱스 값) append

    if answer:
        for start, end in answer:
            length = end - start # 인덱스를 빼준다
            if length < min_length: # 인덱스 값이 min_length 보다 작다면
                min_length = length # min_length에 length을 넣어주고
                result = [start, end] # 해당 인덱스 값을 result에 넣어준다

        return result


solution(sequence, k)