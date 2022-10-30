import sys
rl = sys.stdin.readline

t = int(rl())

for a in range(t):
    n = int(rl())

    li = [False] + [True] * ((n - 1) // 2)
    for x in range(1, int(n**.5/2+1)):
        if li[x]:
            li[2*x*(x+1)::x*2+1] = [False] * ((((n + 1) // 2) -
                                               x * x * 2) // (x * 2 + 1))

    if n == 4:
        i1 = i2 = 2
    elif (n // 2) % 2 == 1:
        i1 = i2 = n // 2
    else:
        i1 = n // 2 - 1
        i2 = n // 2 + 1

    if i1 == 2:
        pass
    else:
        while not (li[i1 // 2] and li[i2 // 2]):
            i1 -= 2
            i2 += 2

    print(i1, i2)


# 1. 짝수 n을 입력 받고, n까지의 소수를 구한다.
# 2. n을 반으로 나눈 후 i씩 더하고 빼면서 두 수 모두 소수인 경우를 찾는다.
