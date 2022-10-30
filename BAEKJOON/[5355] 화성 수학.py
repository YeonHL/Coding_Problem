t = int(input())

for _ in range(t):
    l = input().split()
    for x in range(len(l)):
        if x == 0:
            _num = float(l[0])
        else:
            if l[x] == '@':
                _num *= 3
            elif l[x] == '%':
                _num += 5
            elif l[x] == '#':
                _num -= 7
    print("%.2f" % _num)
