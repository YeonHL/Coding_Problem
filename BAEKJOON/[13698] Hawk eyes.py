s = input()
_small = 1
_big = 4


def Change(a, b, now):
    if now == a:
        return b
    elif now == b:
        return a
    return now


for c in s:
    if c == "A":
        _small = Change(1, 2, _small)
        _big = Change(1, 2, _big)
    elif c == "B":
        _small = Change(1, 3, _small)
        _big = Change(1, 3, _big)
    elif c == "C":
        _small = Change(1, 4, _small)
        _big = Change(1, 4, _big)
    elif c == "D":
        _small = Change(2, 3, _small)
        _big = Change(2, 3, _big)
    elif c == "E":
        _small = Change(2, 4, _small)
        _big = Change(2, 4, _big)
    elif c == "F":
        _small = Change(3, 4, _small)
        _big = Change(3, 4, _big)

print(_small)
print(_big)
