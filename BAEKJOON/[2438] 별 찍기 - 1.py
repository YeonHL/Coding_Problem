import sys

i = int(sys.stdin.readline().rstrip())

for x in range(1, i+1):
    for y in range(x):
        print("*", end="")
    print("")
