import sys
rl = sys.stdin.readline

print(''.join(sorted(rl().rstrip())[::-1]))
