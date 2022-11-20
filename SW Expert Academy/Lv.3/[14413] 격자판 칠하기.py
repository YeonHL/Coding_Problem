# N,M이 모두 1일 경우: 계싼 필요 X
# N 또는 M이 1일 경우: 그 방향만 확인
# 둘다 1이 아닐 경우: 모두 확인


T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    _skip = 0

    _odd = set()
    _even = set()

    for y in range(0, N):
        for x in range(M):
            if board[y][x] == '?':
                continue
            if (x+y) % 2 == 0:
                _even.add(board[y][x])
            elif (x+y) % 2 == 1:
                _odd.add(board[y][x])

    if len(_odd) == 2 or len(_even) == 2 or (len(_odd) == 1 and _odd == _even):
        print(f"#{i} impossible")
    else:
        print(f"#{i} possible")
