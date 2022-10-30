import sys

# C언어 등 다른 언어에서는 개수가 필요하기 때문, Python에서는 사용하지 않아도 된다.
i = int(sys.stdin.readline().rstrip())
l = list(map(int, sys.stdin.readline().rstrip().split()))

print("{0} {1}".format(min(l), max(l)))
