import sys
rl = sys.stdin.readline

n, k = map(int, rl().split())
l = list(map(int, rl().split()))

l.sort()
print(l[-k])
