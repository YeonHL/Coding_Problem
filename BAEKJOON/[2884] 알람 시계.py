a, b = input().split()
a = int(a)
b = int(b)

if b >= 45:
    b -= 45
else:
    b += 15
    if a > 0:
        a -= 1
    else:
        a = 23

print(a, b)
