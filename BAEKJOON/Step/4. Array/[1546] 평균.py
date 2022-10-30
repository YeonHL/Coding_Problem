import sys

n = int(sys.stdin.readline().rstrip())
l = list(map(int, sys.stdin.readline().rstrip().split()))

nl = list()

for i in range(n):
    nl.append(l[i]/max(l)*100)

print(sum(nl) / n)
