import sys
rl = sys.stdin.readline

x = []
y = []
for i in range(3):
    a, b = map(int, rl().split())
    if a in x:
        x.remove(a)
    else:
        x.append(a)
    if b in y:
        y.remove(b)
    else:
        y.append(b)

print(*x, *y)
