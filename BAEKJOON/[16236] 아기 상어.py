# Space에 1부터 순서대로 존재하는지 확인, 존재하지 않을 경우 목표 리스트에 추가 명령 종료


N = int(input())
Space = [list(map(int, input().split())) for _ in range(N)]

# 확인용 코드
print(Space)

Target = [[] for _ in range(6)]

for x in range(N):
    for y in range(N):
        if Space[x][y] in (1, 2, 3, 4, 5, 6):
            Target[Space[x][y]-1].append((x, y))
        elif Space[x][y] == 9:
            _now = (x, y)

print(Target)
print(_now)
