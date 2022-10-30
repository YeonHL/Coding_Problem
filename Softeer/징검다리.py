n = int(input())
a = list(map(int, input().split()))

_now = a[0]
_num = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            _num[i] = max(_num[i], _num[j]+1)

print(max(_num))
