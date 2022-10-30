a, b = input().split()
a = int(a)
b = int(b)
c = int(input())

if b + c >= 60:
    a = (a + (b+c)//60) % 24
    b = (b+c) % 60
else:
    b += c

print(a, b)
