import sys
rl = sys.stdin.readline
wr = sys.stdout.write

n = int(rl())

li = [0] * 10001

for _ in range(n):
    li[int(rl())] += 1

count = 0

for i in range(1, 10001):
    if li[i]:
        for a in range(li[i]):
            wr(i)
        count += li[i]
    elif count == n:
        break
