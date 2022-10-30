#

import sys


def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


rl = sys.stdin.readline

N = int(rl())
N_list = [int(rl()) for _ in range(N)]
N_list.sort()

dif_list = [N_list[i+1] - N_list[i] for i in range(N-1)]
X = dif_list[0]

for x in range(1, N-1):
    X = GCD(X, dif_list[x])

ans_set = set()

for y in range(2, int(X**0.5)+2):
    if X % y == 0:
        ans_set.add(y)
        ans_set.add(X//y)

ans_set.add(X)

print(*sorted(ans_set))
