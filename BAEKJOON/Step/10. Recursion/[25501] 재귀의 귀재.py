import sys
rl = sys.stdin.readline


def Pal(S, i, e, c):
    if (i >= e):
        print(1, c)
    elif (S[i] != S[e]):
        print(0, c)
    else:
        c += 1
        Pal(S, i+1, e-1, c)


t = int(rl())

for _ in range(t):
    s = rl().rstrip()
    Pal(s, 0, len(s)-1, 1)
