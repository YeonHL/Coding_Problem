import sys

l = set()

for i in range(10):
    l.add(int(sys.stdin.readline().rstrip()) % 42)

print(len(l))
