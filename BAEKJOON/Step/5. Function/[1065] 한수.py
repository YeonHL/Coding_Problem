import sys


def Han(x):
    i = 1
    count = 0
    while i <= x:
        if i < 100:
            count += 1
        elif ((i // 100 - i % 100 // 10) == (i % 100 // 10 - i % 10)):
            count += 1
        i += 1

    print(count)


z = int(sys.stdin.readline().rstrip())
Han(z)
