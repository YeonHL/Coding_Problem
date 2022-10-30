import sys

s = sys.stdin.readline().rstrip()
time = 0

for a in s:
    if 65 <= ord(a) <= 67:
        time += 3
    elif 68 <= ord(a) <= 70:
        time += 4
    elif 71 <= ord(a) <= 73:
        time += 5
    elif 74 <= ord(a) <= 76:
        time += 6
    elif 77 <= ord(a) <= 79:
        time += 7
    elif 80 <= ord(a) <= 83:
        time += 8
    elif 84 <= ord(a) <= 86:
        time += 9
    elif 87 <= ord(a) <= 90:
        time += 10

print(time)
