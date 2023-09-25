# 리모컨

import sys
sys.stdin = open('input.txt','r')

n = int(input())
m = int(input())

if m == 0:
    buttons = []
else:
    buttons = list(map(int, input().split()))

minimum = abs(100 - n)

for i in range(999999):
    num = str(i)

    for j in num:
        if int(j) in buttons:
            break

    else:
        minimum = min(minimum, abs(n - i) + len(num))

print(minimum)



# def calc(j):
#     temp = []
#     for i in range(1,6):
#         plus_i = j + 1
#         miuns_i = j - 1
#         if plus_i not in breakdown_num : 
#             temp.append([plus_i, 'plus'])
#         if miuns_i not in breakdown_num:
#             temp.append([miuns_i, 'minus'])
#         if temp != []:
#             break
#     result = []

#     if answer == []:
#         result = temp
#     else:
#         for i in answer:
#             for j in temp:
#                 if j[1] == 'plus':
#                     result = i[0] + j[0],'plus'
#                 else:
#                     result = i[0] + j[0], 'minus'
#     return result

# natural_number = [0,1,2,3,4,5,6,7,8,9]
# start = 100
# num = input()
# breakdown = input()
# answer = []
# answer_1 = []
# qwe = []
# cnt = len(num)
# rst = []
# if int(num) == start:
#     print(0)
# else:
#     if breakdown == 0:
#         print(cnt)
#     else:
#         breakdown_num = list(map(int,input().split()))

# for i in num :
#     i = int(i)
#     if answer == [] :
#         if i not in breakdown_num:
#             answer.append([i,'일반'])
#         else:
#             answer = calc(i)
#         continue

#     for j in answer:
#         if j[1] == '일반':
#             if i not in breakdown_num :
#                 answer.append([j[0] + i, '일반'])
#             else:
#                 answer = calc(i)
#         elif j[1] == 'plus':
#             for k in range(0, 10 , 1):
#                 if k not in breakdown_num :
#                     answer_1.append(i+k)
#             rst.append(min(answer_1))
#             answer_1 = []    
#         elif j[1] == 'minus':
#             for k in range(9, -1, -1):
#                 if k not in breakdown_num :
#                     answer_1.append(i+k)
#             rst.append(max(answer_1))
#             answer_1 = []

# print(answer[0][0])
# print(rst)


# def plus_(i):
#     i += 1
#     if 0 <= i < 10:
#         return i
#     else:
#         return max(LIST_A)
# def minus_(i):
#     i -= 1
#     if 0 <= i < 10:
#         return i
#     else:
#         return min(LIST_A)

# natural_number = [0,1,2,3,4,5,6,7,8,9]
# start = 100
# num = input()
# breakdown = input()
# a = []
# qwe = []
# cnt = len(num)
# if int(num) == start:
#     print(0)
# else:
#     if breakdown == 0:
#         print(cnt)
#     else:
#         breakdown_num = list(map(int,input().split()))
#         LIST_A = [x for x in natural_number if x not in breakdown_num]
#         for i in num:
#             plus = int(i)
#             minus = int(i)
#             for j in breakdown_num:
#                 while 1:
#                     if plus in breakdown_num:
#                         plus = plus_(plus)

#                     if minus in breakdown_num:
#                         minus = minus_(minus)

#                     else:
#                         d = plus
#                         f = minus
#                         break
#             d = str(d)
#             f = str(f)       
#             a.append(d)
#             qwe.append(f)
#         b = int(''.join(a))
#         c = int(''.join(qwe))
#         p = abs(int(num) - b)
#         q = abs(int(num) - c)
#         print(cnt + min(p,q))







