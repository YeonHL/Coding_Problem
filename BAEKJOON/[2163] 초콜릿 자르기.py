# 가로, 세로 중 한 방향으로 먼저 쪼갠다. 1이 됐을 때 총 개수에 대해 나머지 방향으로 쪼갠다
# 1: 0, 2: 1, 3: 2(2,1로 쪼갠 후 1 1 1), 4: 2(2,2로 쪼갠 후 1 1 1 1), 5: 4번 (1 + (2) + (3))
# 짝수일 경우 1 + (2로 나눈 횟수 * 2), 홀수일 경우 1 + (2로 나눈 횟수) + (2로 나누고 1 더한 횟수)

def Distribute(N):
    if N == 1:
        return 0
    else:
        if N % 2:
            return 1 + Distribute(N//2) + Distribute(N//2+1)
        else:
            return 1 + 2 * Distribute(N//2)


n, m = map(int, input().split())
print(Distribute(n)+n*Distribute(m))
