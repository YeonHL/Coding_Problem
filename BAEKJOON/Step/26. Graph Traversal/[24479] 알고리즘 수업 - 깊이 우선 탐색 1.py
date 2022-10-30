import sys
rl = sys.stdin.readline

n, m, r = map(int, rl().split())
Graph = [[] for _ in range(n+1)]
ans = [0] * (n+1)
cur = 1

for _ in range(m):
    u, v = map(int, rl().split())
    Graph[u].append(v)
    Graph[v].append(u)

for l in Graph:
    l.sort()


def dfs(V):
    global cur
    ans[v] = cur
    for to_v in Graph[v]:
        if ans[to_v]:
            continue
        cur += 1
        dfs(to_v)


dfs(r)
for i in ans[1:]:
    print(i)
