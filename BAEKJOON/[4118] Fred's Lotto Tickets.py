while True:
    T = int(input())
    if T == 0:
        break

    _check = [1] + [0] * 49
    for _ in range(T):
        ticket = list(map(int, input().split()))
        for i in ticket:
            _check[i] = 1

    if 0 in _check:
        print("No")
    else:
        print("Yes")
