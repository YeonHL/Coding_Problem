# 원이 맞닿거나 교차하는 경우는 없다. 출발점부터 도착 지점까지 몇개의 원을 벗어나고 들어가는지 계산
# 중점 - 출발점과의 거리와 중점 - 도착점과의 거리가 모두 반지름보다 작다면 pass
# 중점 - 출발점과의 거리와 반지름을 비교, 내부에 있으면 이탈 횟수 +1
# 중점 - 도착점과의 거리와 반지름을 비교, 내부에 있으면 진입 횟수 +1

import sys
rl = sys.stdin.readline

t = int(rl())

for _ in range(t):
    src_x, src_y, dst_x, dst_y = map(int, rl().split())
    n = int(rl())
    planet_list = [list(map(int, rl().split())) for _ in range(n)]

    obit_num = 0

    for i in range(n):
        src_distance = (
            (src_x - planet_list[i][0])**2 + (src_y - planet_list[i][1])**2) ** 0.5
        dst_distance = (
            (dst_x - planet_list[i][0])**2 + (dst_y - planet_list[i][1])**2) ** 0.5
        src_check = planet_list[i][2] > src_distance
        dst_check = planet_list[i][2] > dst_distance

        if src_check and dst_check:
            pass
        elif src_check:
            obit_num += 1
        elif dst_check:
            obit_num += 1

    print(obit_num)
