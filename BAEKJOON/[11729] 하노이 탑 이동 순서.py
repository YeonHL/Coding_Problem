import sys
rl = sys.stdin.readline

cache = {}


def hanoi_top(start, end, n):
    if n == 1:
        return f'{start} {end}'
    if (start, end, n) in cache:
        return cache[(start, end, n)]
    t = 6-start-end
    temp = [hanoi_top(start, t, n-1),
            f'{start} {end}', hanoi_top(t, end, n-1)]
    cache[(start, end, n)] = '\n'.join(temp)
    return cache[(start, end, n)]


n = int(rl())

print(2**n-1)
print(hanoi_top(1, 3, n))


# N=1일 때 S -> D로 한번 이동
# N=2일 때 (N=1일 때 S -> E로 이동) -> (N=1일 때 S -> D로 이동) -> (N=1일 때 E -> D로 이동)
# N=3일 때 (N=2일 때 S -> E로 이동) -> (N=1일 때 S -> D로 이동) -> (N=2일 때 E -> D로 이동)
# N=n일 때 (N=n-1일 때 S-> E로 이동) -> (N=1일 때 S- -> D로 이동) -> (N=n-1일 때 E -> D로 이동)
# hanoi(N-1,S,E,D) -> hanoi(1,S,D,E) -> hanoi(N-1,E,D,S)로 처리


""" def hanoi(N, S, D, E):
    L = []
    if N == 1:
        L.append(str(S) + ' ' + str(D))
        return L
    else:
        return hanoi(N-1, S, E, D) + hanoi(1, S, D, E) + hanoi(N-1, E, D, S)

l = hanoi(n, 1, 3, 2) """
