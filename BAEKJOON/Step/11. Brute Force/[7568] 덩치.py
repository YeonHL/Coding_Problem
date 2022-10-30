# 기본값 1, 몸무게, 키가 모두 큰 변수가 존재할 경우 +1

import sys
rl = sys.stdin.readline

n = int(rl())
people = [list(map(int, rl().split())) for _ in range(n)]

for x in range(n):
    result = 1
    for y in people:
        if people[x][0] < y[0] and people[x][1] < y[1]:
            result += 1
    print(result, end=' ')
