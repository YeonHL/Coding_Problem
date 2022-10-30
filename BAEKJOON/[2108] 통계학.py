import sys
rl = sys.stdin.readline

n = int(rl())
l = []

for _ in range(n):
    l.append(int(rl()))

l.sort()
print(round(sum(l)/n))
print(l[n//2])

_max = 1
_num = []
_count = 1

for i in range(0, len(l)-1):
    _b = l[i]
    if l[i+1] == _b:
        _count += 1
        if i+1 == len(l)-1:
            if _max == _count:
                _num.append(_b)
            elif _max < _count:
                _max = _count
                _num = [_b]
            break
    else:
        if _max == _count:
            _num.append(_b)
        elif _max < _count:
            _max = _count
            _num = [_b]
        _count = 1

_num.sort()

if len(_num) == 1:
    print(_num[0])
elif len(_num) == 0:
    print(l[0])
else:
    print(_num[1])

print(max(l)-min(l))
