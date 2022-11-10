K = int(input())
N = int(input())

_now = 0
for _ in range(N):
    T, Z = input().split()
    _now += int(T)

    if _now > 210:
        continue

    if Z == 'T':
        if K == 8:
            K = 1
        elif K != 8:
            K += 1

print(K)
