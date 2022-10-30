import sys

t = int(sys.stdin.readline().rstrip())

for a in range(t):
    r, s = sys.stdin.readline().rstrip().split()
    r = int(r)

    for b in s:
        for c in range(r):
            print(b, end="")
    print()
