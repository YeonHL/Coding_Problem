import sys
rl = sys.stdin.readline

n = int(rl())
stack = []

for _ in range(n):
    a = rl().split()

    if a[0] == "push":
        stack.append(int(a[1]))
    elif a[0] == "top":
        try:
            print(stack[-1])
        except IndexError:
            print(-1)
    elif a[0] == "size":
        print(len(stack))
    elif a[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "pop":
        try:
            print(stack.pop())
        except IndexError:
            print(-1)
