import sys
rl = sys.stdin.readline

n = int(rl())
l = list(map(int, rl().split()))

print(min(l)*max(l))
