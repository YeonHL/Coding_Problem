import sys
rl = sys.stdin.readline

n = int(rl())
a = list(map(int, rl().split()))

m = int(rl())
b = list(map(int, rl().split()))

c = set(b) - set(a)

print("".join("0 " if x in c else "1 " for x in b))
