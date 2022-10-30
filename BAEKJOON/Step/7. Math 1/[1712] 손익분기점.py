import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())
i = 0

if (c-b) <= 0:
    print(-1)
else:
    print(a // (c-b) + 1)
