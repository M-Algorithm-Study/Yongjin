# 3의 배수

import sys
sys.stdin = open('input.txt','r')

X = input()
cnt = 0

while len(X) > 1:
    Y = 0
    cnt += 1
    for i in X:
        Y += int(i)

    X = str(Y)

print(cnt)
if int(X) % 3 == 0:
    print('YES')
else:
    print('NO')