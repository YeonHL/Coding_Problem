# 두 점의 좌표 및 나머지 한 점과의 거리가 주어진다. 해당 조건을 만족하는 점의 개수가 몇개인지 출력
# 반지름의 합과 두 점 사이의 거리가 같다면 1, 반지름의 합이 두 점 사이의 거리보다 크다면 2, 작다면 0

import sys
rl = sys.stdin.readline

t = int(rl())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, rl().split())

    dis = int(((x2-x1)**2 + (y2-y1)**2)**0.5)

    rs = r1 + r2
    rm = abs(r1-r2)

    if dis == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if dis == rm or dis == rs:
            print(1)
        elif dis < rs or dis > rm:
            print(2)
        else:
            print(0)
