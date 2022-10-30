import sys
rl = sys.stdin.readline

m = int(rl())
n = int(rl())


def cond(x):
    return m <= x <= n


i = 3
prime = [2]

while (i <= n):
    for z in prime:
        if i % z == 0:
            break
        elif z == prime[-1]:
            prime.append(i)
            break

    i += 2

prime_range = list(filter(cond, prime))


if not prime_range:
    print(-1)
else:
    print(sum(prime_range))
    print(prime_range[0])


# 문제 맞춤형으로 코드를 작성한다면 Table을 작성하고 True인 Index의 배수를 모두 False로 만들어서 처리 가능
# 위 코드는 범위에 상관 없이 가능하도록 작성
