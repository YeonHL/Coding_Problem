# 좋아하는 학생이 인접칸에 가장 많은 곳
# -> 비어있는 칸이 가장 많은 곳
# -> 가장 위, 가장 왼쪽을 우선으로 배치된다.

N = int(input())
classroom = [[0]*N for _ in range(N)]
student = [list(map(int, input().split())) for _ in range(N*N)]

# 완전 탐색, 각 자리별 점수를 계산, 가장 큰 곳에 배치
# 점수가 같을 경우 각 자리별 0의 개수를 계산, 가장 많은 곳에 배치
# 0의 개수가 같은 곳이 여러 곳일 경우 가장 앞행의 앞열에 배치


def check_score(Classroom, Favorite, N):
    score = []
    for x in range(N):
        for y in range(N):
            if Classroom[x][y] != 0:
                continue
            cnt = 0
            if x != 0:
                if Classroom[x-1][y] in Favorite:
                    cnt += 1
            if x != N-1:
                if Classroom[x+1][y] in Favorite:
                    cnt += 1
            if y != 0:
                if Classroom[x][y-1] in Favorite:
                    cnt += 1
            if y != N-1:
                if Classroom[x][y+1] in Favorite:
                    cnt += 1

            if cnt == 0:
                score.append([x, y, 0])
            elif cnt == 1:
                score.append([x, y, 1])
            elif cnt == 2:
                score.append([x, y, 10])
            elif cnt == 3:
                score.append([x, y, 100])
            elif cnt == 4:
                score.append([x, y, 1000])

    return score


def check_space(Classroom, N):
    space = []
    for x in range(N):
        for y in range(N):
            if Classroom[x][y] != 0:
                continue
            cnt = 0
            if x != 0:
                if Classroom[x-1][y] == 0:
                    cnt += 1
            if x != N-1:
                if Classroom[x+1][y] == 0:
                    cnt += 1
            if y != 0:
                if Classroom[x][y-1] == 0:
                    cnt += 1
            if y != N-1:
                if Classroom[x][y+1] == 0:
                    cnt += 1

            space.append([x, y, cnt])

    return space


def Calculate_score(Classroom):
    pass


for s in student:
    score = check_score(classroom, s[1:], N)
    score = sorted(score, key=lambda x: (x[2], x[0], x[1]))

    target = []

    for x in score:
        if x[2] == score[0][2]:
            target.append(x)
    if len(target) == 1:
        classroom[score[0][0], score[0][1]] = s[0]
    else:
        space = check_space(classroom, N)
