import sys
rl = sys.stdin.readline

l = set()

for _ in range(int(rl())):
    l.add(rl())

l = list(l)

l.sort()
l.sort(key=lambda x: len(x))

print(''.join(l), end='')
