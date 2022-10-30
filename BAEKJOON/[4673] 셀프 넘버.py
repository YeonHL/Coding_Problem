def d(x):
    return x + (x // 1000) + (x % 1000 // 100) + (x % 100 // 10) + x % 10


def self_number():
    l = list(range(1, 10001))
    for i in range(1, 10001):
        if d(i) in l:
            l.remove(d(i))
    for a in l:
        print(a)


self_number()
