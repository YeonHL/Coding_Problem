import sys
rl = sys.stdin.readline


""" def fib(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    f = [1, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n-1] """


n = int(rl())
l = [1, 2]

for i in range(2, n-1):
    l.append(l[i-2]+l[i-1])

print(l[n-2], n-2)
