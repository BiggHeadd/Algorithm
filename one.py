#coding=utf-8
import sys
import math

def zuida(a, b):
    if a < b:
        a, b = b, a
    while 1:
        y=a%b
        if y==0:
            return b
        a=b
        b=y

def zuixiao(a, b):
    if x>y:
        greater = a
    else:
        greater = b
    while True:
        if (greater % a == 0) and (greater % b == 0):
            icm = greater
            break
        greater+=1
    return greater

def solution(a, b):
    s = a*b
    while a%b!=0:
        a, b = b, (a%b)

    print(b, s//b)

for line in sys.stdin:
    inputs = list(map(int, line.split()))
    x, y = inputs[0], inputs[1]
    if x<1 or y<1 or x>math.pow(2, 32) or y>math.pow(2, 32):
        print("input not in range!")
    else:
        solution(x, y)