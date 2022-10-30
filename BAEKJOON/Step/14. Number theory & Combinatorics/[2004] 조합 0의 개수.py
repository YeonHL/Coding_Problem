# n!의 0의 개수 - m!의 0의 개수 - (n-m)!의 0의 개수
n, m = map(int, input().split())


def check_up_five():
    i = 1
    u_five = 0

    while (n // 5**i):
        u_five += n // (5**i)
        i += 1

    return u_five


def check_down_five():
    i = 1
    d_five = 0

    while (m // 5**i):
        d_five += m // (5**i)
        i += 1

    i = 1

    while ((n-m) // 5**i):
        d_five += (n-m) // (5**i)
        i += 1

    return d_five


def check_up_two():
    i = 1
    u_two = 0

    while (n // 2**i):
        u_two += n // (2**i)
        i += 1

    return u_two


def check_down_two():
    i = 1
    d_two = 0

    while (m // 2**i):
        d_two += m // (2**i)
        i += 1

    i = 1

    while ((n-m) // 2**i):
        d_two += (n-m) // (2**i)
        i += 1

    return d_two


u_five = check_up_five()
u_two = check_up_two()
d_five = check_down_five()
d_two = check_down_two()

print(min(u_five-d_five, u_two-d_two))
