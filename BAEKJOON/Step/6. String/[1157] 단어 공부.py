import sys

s = sys.stdin.readline().rstrip().upper()
m = 0
c = ""

for a in set(s):
    if m < s.count(a):
        c = a
        m = s.count(a)
    elif m == s.count(a):
        c = "?"

print(c)
