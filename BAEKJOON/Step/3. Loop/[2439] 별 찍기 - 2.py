import sys

i = int(sys.stdin.readline().rstrip())
a = i

for x in range(1, i+1):
    for y in range(x):
        while (a > x):
            print(" ", end="")
            a -= 1
        print("*", end="")
    print("")
    a = i
