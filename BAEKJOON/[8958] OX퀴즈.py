import sys

n = int(sys.stdin.readline().rstrip())

total = 0
score = 0

for x in range(n):
    ans = sys.stdin.readline().rstrip()
    for i in ans:
        if i == "O":
            score += 1
        else:
            score = 0
        total += score
    print(total)
    score = 0
    total = 0
