import sys
rl = sys.stdin.readline

x, y, w, h = map(int, rl().split())

print(min(x, w-x, y, h-y))
