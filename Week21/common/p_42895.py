# N으로 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number) :
    answer = -1
    dp = [[] for _ in range(9)]
    for i in range(1, 9) :
        dp[i].append(int(str(N) * i))
        for j in range(1, i) :
            for num1 in dp[j] :
                for num2 in dp[i-j] :
                    dp[i].append(num1 + num2)
                    dp[i].append(num1 - num2)
                    dp[i].append(num1 * num2)
                    if num2 != 0 :
                        dp[i].append(num1 // num2)

        dp[i] = list(set(dp[i]))
        if number in dp[i] :
            return i

    return answer

a = 5
b = 12

print(solution(a,b))