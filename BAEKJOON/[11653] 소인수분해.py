import sys
rl = sys.stdin.readline

n = int(rl())
i = 2

while i*i <= n:
    if not n % i:
        print(i)
        n /= i
    else:
        i += 2 if i > 2 else 1

if n > 1:
    print(int(n))

# i가 소수가 아닐 경우 앞에서 계산한 소수로 이루어졌을 것이므로 나머지가 0이 되지 않을 것이다. 따라서 소수를 따로 구분할 필요는 없다.
# n이 1이 될 때까지 i를 증가시키면서 소인수분해를 진행한다.
# 2를 빼서 계산하는 것과 안에서 if로 계산할 때의 속도는 같다.
