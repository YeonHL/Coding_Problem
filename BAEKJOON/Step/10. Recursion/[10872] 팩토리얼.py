import sys
rl = sys.stdin.readline


def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)


n = int(rl())
print(fac(n))
