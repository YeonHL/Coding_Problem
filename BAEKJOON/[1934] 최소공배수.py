import sys
rl = sys.stdin.readline

# 유클리드 호제법


def GCD(A, B):  # 최대공약수
    if B == 0:
        return A
    return GCD(B, A % B)


T = int(rl())
for i in range(T):
    A, B = map(int, rl().split())
    print(int(A*B/GCD(A, B)))
