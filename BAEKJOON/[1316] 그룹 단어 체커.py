import sys

count = 0
n = int(sys.stdin.readline().rstrip())

for a in range(n):
    s = sys.stdin.readline().rstrip()
    z = set()
    for i in range(len(s)):
        if s[i] in z:
            if s[i] == s[i-1]:
                pass
            else:
                break
        else:
            z.add(s[i])
        if i == len(s)-1:
            count += 1

print(count)
