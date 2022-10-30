# r[0]을 1바퀴 돌렸을 때 다른 원은 몇바퀴를 도는가?
# r[0] / r[i]


import sys
rl = sys.stdin.readline


def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


n = int(rl())
r = list(map(int, rl().split()))

for i in range(1, n):
    d = gcd(r[0], r[i])
    print(''.join([str(r[0]//d), "/", str(r[i]//d)]))
