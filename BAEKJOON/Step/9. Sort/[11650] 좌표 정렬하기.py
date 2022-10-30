import sys
rl = sys.stdin.readline

n = int(rl())

l = []

for _ in range(n):
    a, b = map(int, rl().split())
    l.append((a, b))

l.sort()

for _ in l:
    print("{0} {1}".format(_[0], _[1]))
