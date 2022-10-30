import sys
rl = sys.stdin.readline

a, b = map(int, rl().split())
A = set(rl().split())
B = set(rl().split())

print(len(A)+len(B)-2*len(A & B))
