import sys
rl = sys.stdin.readline

# 유클리드 호제법


def GCD(M, N):  # 최대공약수
    if N == 0:
        return M
    return GCD(N, M % N)


M, N = map(int, rl().split())
print(GCD(M, N))

# 최소공배수
print(int(M*N/GCD(M, N)))


""" i = 2
a, b = map(int, rl().split())

_min = min(a, b)
_max = max(a, b)

a_set = {1}
b_set = {1}

while (i <= _min):
    if a % i == 0:
        a_set.add(i)
    if b % i == 0:
        b_set.add(i)

    i += 1

x = _min
z = 2

while (x % _max != 0):
    x = _min*z
    z += 1

print(max(a_set & b_set))
print(x)
 """
