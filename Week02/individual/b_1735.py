# 분수 합

import sys
from fractions import Fraction
sys.stdin = open('input.txt','r')

A, B = map(int,input().split())
C, D = map(int,input().split())

Q = Fraction(A,B)
W = Fraction(C,D)

T = Fraction(Q + W) 
print(T.numerator, T.denominator)
