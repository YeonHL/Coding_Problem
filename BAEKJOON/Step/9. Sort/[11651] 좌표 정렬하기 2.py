import sys
rl = sys.stdin.readline

n = int(rl())
l = []

for _ in range(n):
    l.append(rl())

l.sort(key=lambda x: int(x.split()[0]))
l.sort(key=lambda x: int(x.split()[1]))

print(''.join(l))
