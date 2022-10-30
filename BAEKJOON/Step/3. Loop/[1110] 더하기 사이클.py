import sys

i = int(sys.stdin.readline().rstrip())
n = i
iter = 0

while (True):
    if n < 10:
        n * 10
    x = (n // 10) + (n % 10)
    n = (n % 10) * 10 + (x % 10)

    iter += 1
    if n == i:
        break

print(iter)
