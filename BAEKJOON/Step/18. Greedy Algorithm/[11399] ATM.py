# _line 내 원소 정렬
# _now와 _sum을 따로 계산

n = int(input())
_line = sorted(list(map(int, input().split())))

_now = 0
_sum = 0
for i in _line:
    _now += i
    _sum += _now

print(_sum)
