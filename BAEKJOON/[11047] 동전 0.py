import sys
rl = sys.stdin.readline

n, k = map(int, rl().split())

l = [int(rl()) for _ in range(n)]

_count = 0
_remain = k

for i in range(n-1, -1, -1):
    if _remain // l[i] >= 1:
        _count += (_remain // l[i])
        _remain -= (_remain // l[i] * l[i])
    if _remain == 0:
        break

print(_count)
