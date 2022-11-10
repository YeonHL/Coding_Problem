s = input()
n = len(s)
_check = 1

for i in range(n):
    if s[i] != s[n-1-i]:
        _check = 0
        break

print(_check)
