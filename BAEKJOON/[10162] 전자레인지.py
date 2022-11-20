T = int(input())
A = B = C = 0

if T % 10 != 0:
    print(-1)
else:
    if T >= 300:
        A = T // 300
        T %= 300

    if T >= 60:
        B = T // 60
        T %= 60

    if T >= 10:
        C = T // 10
        T %= 10

    print(A, B, C)
