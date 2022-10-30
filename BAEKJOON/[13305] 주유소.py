# 1. 처음 위치에서 더 싼곳이 나올 때까지 거리를 계속 더한다.
# 2. 더 싼 곳이 나오면 처음 위치의 리터당 가격 * 이동 거리를 계산하고 더 싼 주유소의 가격으로 1번을 반복한다.
# 3. 도착했을 경우 최종 값 출력

n = int(input())
_meter = list(map(int, input().split()))
_price = list(map(int, input().split()))

_min = _price[0]
_sum = 0
_now = 0
for i in range(0, n-1):
    _now += _meter[i]
    if _price[i+1] < _min:
        _sum += (_now*_min)
        _now = 0
        _min = _price[i+1]
    elif i+1 == n-1:
        _sum += (_now*_min)
print(_sum)
