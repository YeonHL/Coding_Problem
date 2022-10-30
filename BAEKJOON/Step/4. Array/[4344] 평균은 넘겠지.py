import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    l = list(map(int, sys.stdin.readline().rstrip().split()))
    avg = sum(l[1:l[0]+1]) / l[0]
    number = 0
    for x in l[1:l[0]+1]:
        if x > avg:
            number += 1
    print(format(number/l[0]*100, ".3f"), end="")
    print("%")
