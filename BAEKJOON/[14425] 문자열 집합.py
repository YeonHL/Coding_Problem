import sys
rl = sys.stdin.readline

N, M = map(int, rl().split())

_string = {rl().rstrip() for _ in range(N)}
_count = 0

for _ in range(M):
    if rl().rstrip() in _string:
        _count += 1

print(_count)
