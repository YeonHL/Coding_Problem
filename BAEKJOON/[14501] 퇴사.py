import sys
rl = sys.stdin.readline

N = int(rl())
schedule = [[0, 0]] + [list(map(int, rl().split())) for _ in range(N)]
income = [0] * (N+1)

for i in range(1, N+1):
    _end = schedule[i][0]+i-1
    if _end <= N:
        income[_end] = max(income[_end], income[i-1]+schedule[i][1])
    income[i] = max(income[:i+1])

print(max(income))
