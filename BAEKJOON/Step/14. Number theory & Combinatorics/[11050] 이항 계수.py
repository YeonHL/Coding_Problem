import sys
rl = sys.stdin.readline

n, k = map(int, rl().split())
u = 1
d = 1

while k:
    u *= n
    d *= k
    n -= 1
    k -= 1

print(u // d)
