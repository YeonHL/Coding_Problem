M = int(input())
_now = 1

for _ in range(M):
    a, b = map(int, input().split())
    if a == _now:
        if b not in (1, 2, 3):
            _now = -1
            break
        _now = b
    elif b == _now:
        if a not in (1, 2, 3):
            _now = -1
            break
        _now = a

print(_now)
