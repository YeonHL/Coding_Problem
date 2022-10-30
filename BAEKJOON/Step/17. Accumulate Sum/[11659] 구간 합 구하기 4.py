import sys
rl = sys.stdin.readline

n, m = map(int, rl().split())
l = list(map(int, rl().split()))

sum_table = [l[0]]

for x in range(1, n):
    sum_table.append(l[x] + sum_table[x-1])

for _ in range(m):
    i, j = map(int, rl().split())
    if i == 1:
        print(sum_table[j-1])
    else:
        print(sum_table[j-1] - sum_table[i-2])
