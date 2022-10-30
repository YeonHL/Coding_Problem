import sys
rl = sys.stdin.readline

l = []

for _ in range(int(rl())):
    l.append(rl().rstrip())

l.sort(key=lambda x: int(x.split()[0]))

print('\n'.join(l))
