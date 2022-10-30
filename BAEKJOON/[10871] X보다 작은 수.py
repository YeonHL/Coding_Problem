import sys

n, x = sys.stdin.readline().rstrip().split()
n = int(n)
x = int(x)

l = sys.stdin.readline().rstrip().split()

for i in range(n):
    if int(l[i]) < x:
        print(int(l[i]), end=" ")
