import sys

a = int(sys.stdin.readline().rstrip())
n = sys.stdin.readline().rstrip()

sum = 0

for i in n:
    sum += int(i)

print(sum)
