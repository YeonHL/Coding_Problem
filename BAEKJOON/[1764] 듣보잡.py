import sys
rl = sys.stdin.readline

n, m = map(int, rl().split())

_listen = {rl().rstrip() for i in range(n)}
_see = {rl().rstrip() for i in range(m)}

ans = sorted(_listen & _see)

print(len(ans))
for x in ans:
    print(x)
