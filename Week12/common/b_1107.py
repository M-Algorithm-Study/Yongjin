# 리모컨
# 마지막 예시에서 틀린다..
# 방법을 바꿔서 해보자
# -1 , +1 씩 while를 통해 cnt로 접근해보자
import sys
sys.stdin = open('input.txt','r')

def plus_(i):
    i += 1
    if 0 <= i < 10:
        return i
    else:
        return max(LIST_A)
def minus_(i):
    i -= 1
    if 0 <= i < 10:
        return i
    else:
        return min(LIST_A)

natural_number = [0,1,2,3,4,5,6,7,8,9]
start = 100
num = input()
breakdown = input()
a = []
qwe = []
cnt = len(num)
if int(num) == start:
    print(0)
else:
    if breakdown == 0:
        print(cnt)
    else:
        breakdown_num = list(map(int,input().split()))
        LIST_A = [x for x in natural_number if x not in breakdown_num]
        for i in num:
            plus = int(i)
            minus = int(i)
            for j in breakdown_num:
                while 1:
                    if plus in breakdown_num:
                        plus = plus_(plus)

                    if minus in breakdown_num:
                        minus = minus_(minus)

                    else:
                        d = plus
                        f = minus
                        break
            d = str(d)
            f = str(f)       
            a.append(d)
            qwe.append(f)
        b = int(''.join(a))
        c = int(''.join(qwe))
        p = abs(int(num) - b)
        q = abs(int(num) - c)
        print(cnt + min(p,q))

