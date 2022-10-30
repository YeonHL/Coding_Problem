import sys
rl = sys.stdin.readline

N, M = map(int, rl().split())
Pokemon = []
_Dict = {}

for i in range(N):
    Pokemon.append(rl().rstrip())
    _Dict[Pokemon[i]] = i+1


for _ in range(M):
    ans = rl().rstrip()
    try:
        print(Pokemon[int(ans)-1])
    except ValueError:
        print(_Dict[ans])
