def Cal(a, b, C):
    if C == "+":
        return a+b
    elif C == "*":
        return a*b


a = int(input())
C = input()
b = int(input())

print(Cal(a, b, C))
