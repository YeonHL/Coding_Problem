# 1번

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

""" def solution(N):
    # write your code in Python 3.6
    n = str(N)
    _max = -999999
    for x in range(len(n)):
        if n[x] == '5':
            if x == len(n)-1:
                _now = int(n[:x])
            else:
                _now = int(n[:x]+n[x+1:])
            if _now > _max:
                _max = _now
    return _max """


# N 입력, 값 중 하나의 5를 제거했을 때 가장 큰 값
# for x in range(len(str(N))
# if  == '5':
#    _now = int()

# return _max

# 2번

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

""" def solution(A):
    # write your code in Python 3.6
    _max = 1
    for x in list(set(A)):
        c = A.count(x)
        if c > _max:
            _max = c
    
    for i in range(1,max(A)-min(A)+1):
        for s in set(A):
            _count = 1

            while s + i in A:
                s += i
                _count += 1

            if _count > _max:
                _max = _count

    return _max """

# N개의 정수를 갖는 A 배열에서 오름차순으로 선택하며 등차로 선택했을 때 가장 많은 숫자를 포함하는 쌍을 반환한다.
# 선택한 정수의 총 갯수를 출력한다.

# 3번


""" from collections import deque

def solution(B):
    A = []
    n = len(B)
    m = len(B[0])

    for b in range(n):
        B[b] = list(B[b])
        if 'A' in B[b]:
            A = [b, B[b].index('A')]

    for r in range(n):
        for c in range(m):
            if B[r][c] == 'v':
                B[r][c] = 'X'
                for i in range(r+1, n):
                    if B[i][c] == 'X' or B[i][c] == '>' or B[i][c] == '<' or B[i][c] == '^' or B[i][c] == 'v':
                        break
                    elif B[i][c] == 'A':
                        return False
                    B[i][c] = 'O'
            elif B[r][c] == '^':
                B[r][c] = 'X'
                for i in range(0, r):
                    if B[i][c] == 'X' or B[i][c] == '>' or B[i][c] == '<' or B[i][c] == '^' or B[i][c] == 'v':
                        break
                    elif B[i][c] == 'A':
                        return False
                    B[i][c] = 'O'
            elif B[r][c] == '<':
                B[r][c] = 'X'
                for i in range(0, c):
                    if B[r][i] == 'X' or B[r][i] == '>' or B[r][i] == '<' or B[r][i] == '^' or B[r][i] == 'v':
                        break
                    elif B[r][i] == 'A':
                        return False
                    B[r][i] = 'O'
            elif B[r][c] == '>':
                B[r][c] = 'X'
                for i in range(c+1, m):
                    if B[r][i] == 'X' or B[r][i] == '>' or B[r][i] == '<' or B[r][i] == '^' or B[r][i] == 'v':
                        break
                    elif B[r][i] == 'A':
                        return False
                    B[r][i] = 'O'

    q = deque([A])
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    visited = [[0] * m for i in range(n)]
    visited[A[0]][A[1]] = 1

    while q:
        px, py = q.popleft()

        for k in range(4):
            mx = px + dx[k]
            my = py + dy[k]
            if 0 <= mx < n and 0 <= my < m:
                if B[mx][my] == '.' and not visited[mx][my]:
                    visited[mx][my] = 1 
                    q.append((mx, my))
            
    if visited[-1][-1] == 1:
        return True
    else:
        return False """


# 이차원 배열 N행, M열, '.'은 공백을 나타내며 X는 장애물, A는 경비병이다.
# 각각의 경비병은 자신의 위치에서 바로보고 있는 방향의 직선에 있는 모든 것을 본다.
# 암살자가 그의 위치로부터 우측 하단까지 이동할 때 들키지 않는다면 True, 아니면 False를 반환한다.
A = []

B = ['X.....>', '..v..X.', '.>..X..', 'A......']

""" B = ['...Xv',
     'AX..^',
     '.XX..'] """

for b in range(len(B)):
    B[b] = list(B[b])
    if 'A' in B[b]:
        A = [b, B[b].index('A')]
    print(A)

for r in range(len(B)):
    for c in range(len(B[r])):
        if B[r][c] == 'v':
            for i in range(r, len(B)):
                if B[i][c] == 'X' or '>' or '<' or '^' or 'v':
                    break
                B[i][c] = 'O'
        elif B[r][c] == '^':
            for i in range(0, r+1):
                if B[i][c] == 'X' or '>' or '<' or '^' or 'v':
                    break
                B[i][c] = 'O'
        elif B[r][c] == '<':
            for i in range(0, c+1):
                if B[r][i] == 'X' or '>' or '<' or '^' or 'v':
                    break
                B[r][i] = 'O'
        elif B[r][c] == '>':
            for i in range(c, len(B[r])):
                if B[r][i] == 'X' or '>' or '<' or '^' or 'v':
                    break
                B[r][i] = 'O'


for b in B:
    print(b)
