n, m = map(int, input().split())

a = [input().split() for _ in range(n)]
b = [input().split() for _ in range(n)]
_result = [[] for _ in range(n)]

for x in range(n):
    for y in range(m):
        _result[x].append(str(int(a[x][y])+int(b[x][y])))

for x in range(n):
    print(' '.join(_result[x]))
