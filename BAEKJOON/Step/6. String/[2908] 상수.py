import sys


def sang(n):
    return (n % 10 * 100) + (n % 100 - n % 10) + (n // 100)


a, b = map(int, sys.stdin.readline().rstrip().split())

print(max(sang(a), sang(b)))
