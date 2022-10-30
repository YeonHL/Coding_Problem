# P명의 사람 중 몇명이 링크 내에 있는지 출력
# 반복문, Link 내에 있으면 숫자 +1
# x~x+w, y~y+h의 직사각형의 양쪽 끝에 중점이 (x,y+h/2), (x+w,y+h/2)이고
# 반지름이 h/2인 반원이 붙어있는 형태이다.

import sys
rl = sys.stdin.readline

w, h, x, y, p = map(int, rl().split())
_count = 0

for i in range(p):
    a, b = map(int, rl().split())
    if x <= a <= x+w and y <= b <= y+h:
        _count += 1
    elif ((x-a)**2 + (y+h/2-b)**2)**0.5 <= h/2 or ((x+w-a)**2 + (y+h/2-b)**2)**0.5 <= h/2:
        _count += 1

print(_count)
