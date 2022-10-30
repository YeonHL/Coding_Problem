# 모든 경우의 수에 따른 금액 계산하기
# 게산한 금액 중 가장 큰 것 선택하기
# 불가능한 선택지는 제거하기

# 시작 일자와 종료 일자를 받는 함수 만들기
# i일차에서 T일 동안 상담한다고 가정, T일 동안 가능한


import sys
rl = sys.stdin.readline

n = int(rl())
schedule_list = [[]]

for _ in range(n):
    schedule_list.append(list(map(int, rl().split())))

for i in range(1, n+1):
    if schedule_list[i][0] + i-1 > n:
        pass
    else:
