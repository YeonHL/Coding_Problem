import sys
rl = sys.stdin.readline

a = b = c = d = 1

while True:
    a, b, c, d = map(int, rl().split())
    if a == b == c == d == 0:
        break

    cnt = 0

    while not a == b == c == d:
        a, b, c, d = abs(a-b), abs(b-c), abs(c-d), abs(d-a)
        cnt += 1

    print(cnt)
