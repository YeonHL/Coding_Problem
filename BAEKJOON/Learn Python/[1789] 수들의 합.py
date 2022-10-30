# n(n+1) / 2가 s보다 작은 최대의 n

s = int(input())
n = int(s**0.5)-1

_sum = n*(n+1)//2

while (_sum <= s):
    n += 1
    _sum = n*(n+1)//2

n -= 1

print(n)
