import sys

x = int(sys.stdin.readline().rstrip())

for i in range(x):
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    b = int(b)
    print(a+b)
