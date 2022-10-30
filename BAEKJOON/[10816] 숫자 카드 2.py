import sys
rl = sys.stdin.readline

N = int(rl())
Card = rl().split()

M = int(rl())
Find = rl().split()

Table = [0] * 20000001

for i in Card:
    Table[int(i)+10000000] += 1

for x in Find:
    print(Table[int(x)+10000000], end=' ')