s = int(input())
i = int(input())
sum = 0

for x in range(i):
    a, b = input().split()
    a = int(a)
    b = int(b)
    sum += a*b

if (sum == s):
    print("Yes")
else:
    print("No")
