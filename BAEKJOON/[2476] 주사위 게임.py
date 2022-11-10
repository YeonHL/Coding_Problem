n = int(input())
Price = []
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        Price.append(10000 + a*1000)
    elif a == b or a == c:
        Price.append(1000 + a*100)
    elif b == c:
        Price.append(1000 + b*100)
    else:
        Price.append(max(a, b, c)*100)

print(max(Price))
