import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    H, W, N = map(int, sys.stdin.readline().rstrip().split())
    print(((N-1) // H + 1) + (((N-1) % H + 1) * 100))


# 101호부터 H01호까지, 이후 102호부터 HW호까지
