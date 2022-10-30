# 시간을 시작과 종료 시간으로 리스트에 저장
# 종료 시간을 기준으로 정렬, 같은 값들은 시작 시간 기준으로 정렬
# 종료 시간을 기준으로 비교, 만약 종료 시간이 더 이전인 회의가 있으면 그 종료 시간을 저장, 카운트 + 1
# 무조건 heapq를 사용해야 하는 문제

import sys
from heapq import heappush, heappop, heapify

rl = sys.stdin.readline

n = int(rl())
heap = []

for _ in range(n):
    s, f = map(int, rl().split())
    heappush(heap, (f, s))

v = 0
cnt = 0
while heap:
    f, s = heappop(heap)
    if s >= v:
        cnt += 1
        v = f

print(cnt)

""" import sys

n = int(sys.stdin.readline())
_time = dict()
_same = dict()
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a == b:
        if a not in _same:
            _same[a] = 1
        else:
            _same[a] += 1
    elif a not in _time:
        _time[a] = b
    elif _time[a] > b:
        _time[a] = b

_time = list(_time.items())

for x in _same:
    for _ in range(_same[x]):
        _time.append((x, x))

_time = sorted(_time, key=lambda x: (x[1], x[0]))
f = _time[0][1]

_count = 1


for i in _time:
    if i[0] >= f:
        _count += 1
        f = i[1]

print(_count) """
