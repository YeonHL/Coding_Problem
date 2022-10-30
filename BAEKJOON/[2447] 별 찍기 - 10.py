# 3의 제곱으로 입력
# 1: 기본 출력, 2: 1을 9번 출력, 3: 2를 9번 출력
# star_list에 *과 공백을 저장하여 마지막에 출력한다.
# 리스트에 추가하는 줄 입력, for문으로 3칸, N/3 단위로 3줄에 입력하기
# 함수를 9번 호출, N=1이 됐을 경우 별을 입력하기 시작하고 그 전까지는 star(N/3)를 다시 호출
# R은 현재 몇번째 행인지, C는 3분할했을 때 몇번째 열인지를 나타낸다.

import sys
rl = sys.stdin.readline

n = int(rl())
star_list = [''] * n


def star(N, R, C):
    if (R % (3*N)) == N and C == 1:
        for i in range(N):
            star_list[R+i] += ' '*N
    else:
        if N == 1:
            star_list[R] += '*'
        else:
            for r in range(0, N, N//3):
                for c in range(3):
                    star(N//3, R+r, c)


star(n, 0, 0)
print("\n".join(star_list))
