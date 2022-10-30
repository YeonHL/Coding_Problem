import sys
rl = sys.stdin.readline

while True:
    l = list(map(int, rl().split()))
    if l[0] == l[1] == l[2] == 0:
        break

    _max = max(l)
    l.remove(max(l))

    _sum = l[0] ** 2 + l[1] ** 2
    if _max ** 2 == _sum:
        print("right")
    else:
        print("wrong")
