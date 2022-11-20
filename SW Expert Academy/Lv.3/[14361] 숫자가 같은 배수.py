# 재배열해서 배수를 구해야하므로 같은 자리 수로 제한 두기 (len)
# len의 길이가 같을 때까지 배수를 구하고 각 자리 숫자를 list로 나누면서
# list가 같은 경우가 있으면 possible, 없으면 impossible

T = int(input())

for test_case in range(1, T + 1):
    N = input()
    _list = sorted(list(N))
    _check = 0

    i = 2
    while True:
        _now = str(int(N) * i)

        if len(N) != len(_now):
            break

        if sorted(list(_now)) == _list:
            _check = 1
            break

        i += 1

    if _check == 1:
        print(f"#{test_case} possible")
    elif _check == 0:
        print(f"#{test_case} impossible")
