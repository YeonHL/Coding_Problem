n = int(input())
m = int(input())

_now = m
ans = m

for _ in range(n):
    a, b = map(int, input().split())
    _now += (a-b)

    if _now > ans:
        ans = _now

    if _now < 0:
        ans = 0
        break

print(ans)
