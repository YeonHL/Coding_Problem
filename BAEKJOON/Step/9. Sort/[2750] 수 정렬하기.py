import sys
rl = sys.stdin.readline

n = int(rl())

li = list()

for i in range(n):
    li.append(int(rl()))

li.sort()
for l in li:
    print(l)
