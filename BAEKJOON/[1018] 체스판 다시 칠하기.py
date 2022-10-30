# _cut으로 8*8로 가능한 경우에 모두 접근 -> 구현
# 8*8에 접근하여 칠해야 하는 수를 계산하여 저장, 최소값과 비교하여 더 작으면 그 값에 저장
# WBWBWBWB, BWBWBWBW 순으로 접근했을 때의 색칠 수와 64 - 색칠 수 중 적은 수 반환
# 나머지 계산,
# 반환한 값과 저장된 min 비교, 둘 중 작은 값 저장

import sys
rl = sys.stdin.readline

n, m = map(int, rl().split())
_board = [rl().rstrip() for _ in range(n)]

_min = 64

for x in range(n-7):
    for y in range(m-7):
        _cut = []
        _count = 0
        for a in range(8):
            _cut.append(_board[x+a][y:y+8])

        _first = _cut[0][0]

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    if _cut[i][j] != _first:
                        _count += 1
                else:
                    if _cut[i][j] == _first:
                        _count += 1

        _count = min(_count, 64-_count)

        if _count < _min:
            _min = _count

print(_min)
