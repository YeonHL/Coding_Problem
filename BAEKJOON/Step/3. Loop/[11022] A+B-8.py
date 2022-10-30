import sys

i = int(sys.stdin.readline().rstrip())

for x in range(1, i+1):
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    b = int(b)
    print("Case #{0}: {1} + {2} = {3}".format(x, a, b, a+b))
