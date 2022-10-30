# 1. 처음으로 발견된 #의 위치 찾기
# 2. 해당 줄의 #의 개수를 세고 연속으로 존재하는 #의 개수와 일치하는지 확인
# 3. 해당 위치로부터 우측 끝, 하단 끝까지 bfs를 돌면서 연속된 #의 개수 계산, . 이후에 다시 #이 나오면 False
# 4.

""" x_locate = 0
_pass = 0
for x in board:
    if '#' in x:
        y_num = x.count('#')
        y_locate = x.index('#')
        break
    x_locate += 1
x_num = 0
for a in board[x_locate:]:
    if '#' not in a:
        break
    _cnt = 0
    for b in a[y_locate:]:
        if b == '#':
            _cnt += 1
        else:
            break
    x_num += 1
    if _cnt != y_num:
        _pass = 1
        break """
""" T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    board = [input() for _ in range(n)]
    x_locate = 0
    _pass = 0
    for x in board:
        if '#' in x:
            y_num = x.count('#')
            y_locate = x.index('#')
            break
        x_locate += 1
    x_num = 0
    for a in board[x_locate:]:
        if '#' not in a:
            break
        _cnt = 0
        for b in a[y_locate:]:
            if b == '#':
                _cnt += 1
            else:
                break
        x_num += 1
        if _cnt != y_num:
            _pass = 1
            break

    if _pass == 1:
        print(f"#{test_case} no")
    elif x_num != y_num:
        print(f"#{test_case} no")
    else:
        print(f"#{test_case} yes") """

""" t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    p = 0
    _exist = 0

    for i in range(n):
        if '#' in board[i]:
            if _exist == 0:
                _exist = 1
                _string = board[i]
                b = board[i].count('#')
                x = i
                y = board[i].index('#')
            else:
                if _string != board[i]:
                    p = 1
                    break

    if p == 1:
        pass
    elif x + b > n or y + b > n:
        p = 1
    else:
        for c in range(x, x+b):
            for d in range(y, y+b):
                if board[c][d] != '#':
                    p = 1

    if p == 1:
        print(f"#{test_case} no")
    else:
        print(f"#{test_case} yes")

    p = 0
    _check = ''
    for x in range(n):
        if p == 1:
            break
        if '#' in board[x]:
            if len(_check) != 0:
                if _check != board[x]:
                    p = 1
                    break
            else:
                _check = board[x]
                l = board[x].count('#')
                a = board[x].index('#')
                if a + l > n:
                    p = 1
                    break
                else:
                    for i in range(a, l+a):
                        if board[x][i] != '#':
                            p = 1
                            break
                _num = x

    if not p and (_num == n or _num+l > n):
        p = 1
    else:
        for t in range(1, l):
            if board[_num+t] != _check:
                p = 1
                break

    if p == 1:
        print(f"#{test_case} no")
    else:
        print(f"#{test_case} yes")
 """

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    Check = True

    graph = [list(input()) for _ in range(N)]
    coordinates = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == '#':
                coordinates[i].append(j)
    res = []

    for i in coordinates:
        if len(i) > 0:
            res.append(i)
    ans = res[0]

    if len(ans) != len(res):
        Check = False
    else:
        if len(ans) == 1:
            Check = True
        else:
            for i in range(1, len(res)):
                if res[i] != res[i-1]:
                    Check = False
                    break
            for i in range(1, len(ans)):
                if ans[i] != ans[i - 1] + 1:
                    Check = False
                    break

    print(f"#{t} yes" if Check else f"#{t} no")
