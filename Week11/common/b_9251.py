# LCS

import sys
sys.stdin = open('input.txt','r')

word = input()
word_1 = input()
a = [0] * len(word_1)

for i in range(len(word)):
    cnt = 0
    for j in range(len(word_1)):
        if cnt < a[j] :
            cnt = a[j]
        elif word[i] == word_1[j]:
            a[j] = cnt + 1

print(max(a))


# word = input()
# word_1 = input()
# x = 0
# a = []

# for i in range(len(word)):
#     for j in range(x , len(word_1)):
#         if word[i] == word_1[j]:
#             a.append(word[i])
#             x = j
#             break

# print(len(a))
