import sys
rl = sys.stdin.readline

while (True):
    a, b = map(int, rl().split())

    if a == b == 0:
        break

    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")
