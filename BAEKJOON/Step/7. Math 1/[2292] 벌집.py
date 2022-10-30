import sys

n = int(sys.stdin.readline().rstrip())
i = 1
number = 1

while (n > number):
    number += 6*i
    i += 1

print(i)
