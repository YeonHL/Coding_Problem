# 풀이 방법 1. try-except

import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(a+b)
    except:
        break


# 풀이 방법 2. readlines

""" lines = sys.stdin.readlines()

for line in lines:
    A, B = map(int, line.split())
    print(A+B) """
