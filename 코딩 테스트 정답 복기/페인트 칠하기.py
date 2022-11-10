import sys
rl = sys.stdin.readline

# 차량의 대수, 반경, 도료량
N, R, Q = map(int, rl().split())

# 좌표, 필요 도료량 리스트
X_P = sorted([list(map(int, rl().split())) for _ in range(N)])


cnt = 0

# 1. 모든 요구 도료량이 0이 될 때까지 반복
''' for y in range(N):
    if X_P[y][1] == 0:
        continue
    Paint = X_P[y][1] // Q + 1 
    radius = X_P[y][0] + 2*R

    for x in range(y,N):
        if X_P[x][0] > radius:
            break
        if X_P[x][1] < Paint*Q :
            X_P[x][1] = 0
        else:
            X_P[x][1] -= (Paint * Q)
    
    cnt += Paint '''

# 2. 도료량을 충족했을 경우 제거, 남은 리스트로 계산하면서 모두 충족되면 종료
while True:
    Paint = X_P[0][1] // Q + 1
    radius = X_P[0][0] + 2*R
    X_P.remove(X_P[0])

    i = 0
    while True:
        if i == len(X_P):
            break
        if X_P[i][0] > radius:
            break
        if X_P[i][1] <= Paint*Q:
            X_P.remove(X_P[i])
            i -= 1
        else:
            X_P[i][1] -= (Paint * Q)

        i += 1

    cnt += Paint

    if len(X_P) == 0:
        break


print(cnt)
