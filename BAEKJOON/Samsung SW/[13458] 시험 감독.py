# N개의 시험장
# 각 시험장에는 a명씩 있다
# 각각의 시험장의 1명의 총감독관은 인당 b명씩 감시할 수 있고 부감독관은 인당 c명씩 감시할 수 있다.
# 각 시험장에 몇명의 감독관이 필요한지 구하고 총 감독관 수의 합을 반환

import sys
rl = sys.stdin.readline

n = int(rl())

a = list(map(int, rl().split()))
b, c = map(int, rl().split())

_sum = 0

for i in range(n):
    if a[i] > b:
        if (a[i]-b) % c == 0:
            _sum += (a[i]-b) // c + 1
        else:
            _sum += (a[i]-b) // c + 2

    else:
        _sum += 1

print(_sum)
