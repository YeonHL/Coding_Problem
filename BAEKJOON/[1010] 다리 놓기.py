# 많은 것 중 적은 것의 개수만큼 고르기

import sys
rl = sys.stdin.readline

t = int(rl())

for _ in range(t):
    n, m = map(int, rl().split())

    u = 1
    d = 1

    while n:
        u *= m
        d *= n
        m -= 1
        n -= 1

    print(u//d)
