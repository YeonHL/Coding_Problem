# 방향이 북이나 남쪽인 것 중 가장 큰 것과 서,동쪽인 것 중 가장 작은 것의 곱을 구한다.
#

import sys
rl = sys.stdin.readline

k = int(rl())
_list = [list(map(int, rl().split())) for _ in range(6)]

max_x = 0
max_y = 0

for i in range(6):
    if (_list[i][0] == 1 or _list[i][0] == 2) and _list[i][1] > max_x:
        max_x = _list[i][1]
    elif (_list[i][0] == 3 or _list[i][0] == 4) and _list[i][1] > max_y:
        max_y = _list[i][1]
    if _list[i][0] == _list[i-2][0] and _list[(i+1) % 6][0] == _list[(i-1)][0]:
        _empty = _list[i-1][1] * _list[i][1]

print(k*((max_x*max_y)-_empty))
