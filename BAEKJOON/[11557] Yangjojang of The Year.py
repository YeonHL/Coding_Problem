for _ in range(int(input())):
    univ = ""
    _max = 0
    for _ in range(int(input())):
        a, b = input().split()
        if int(b) > _max:
            univ = a
            _max = int(b)

    print(univ)
