# N!에 10이 몇개가 생기는지를 확인하면 된다.
# 2는 개수가 많으므로 사실상 5의 개수가 곧 0의 개수이다.

N = int(input())
i = 1

_count = 0

while N // (5**i) != 0:
    _count += N//(5**i)
    i += 1

print(_count)
