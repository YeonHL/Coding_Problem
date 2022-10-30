import sys
rl = sys.stdin.readline

_str = rl().rstrip()
substr = set()

n = (len(_str))

for i in range(n):
    for j in range(1, n-i+1):
        substr.add(_str[i:i+j])

print(len(substr))
