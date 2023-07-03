# 어려워서 유튜브 보고 이해하려고 노력했습니다

def parse(str):
    correct = True
    left = 0
    right = 0
    mystack = []
    
    for i in range(len(str)):
        if str[i] == '(':
            left += 1
            mystack.append('(')
        else:
            right += 1
            if len(mystack) == 0:
                correct = False
            else:
                mystack.pop()
                
        if left == right:
            return i + 1, correct
    return 0, False

def solution(p):
    if len(p) == 0: # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
        return p
    
    pos, correct = parse(p) # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    u = p[:pos] # p 의 처음부터 pos까지
    v = p[pos:] # p 의 pos부터 끝까지
    
    if correct: # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
        return u + solution(v)  # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    

    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    answer = '(' + solution(v) + ')'  # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다./ 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. / 4-3. ')'를 다시 붙입니다. 
    for i in range(1, len(u)-1): # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        if u[i] == '(':
            answer += ')'
        else:
            answer += '('
        
    return answer # 4-5. 생성된 문자열을 반환합니다.
