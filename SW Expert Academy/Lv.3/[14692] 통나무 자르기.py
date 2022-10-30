t = int(input())

for _ in range(1, t+1):
    n = int(input())
    if n % 2 == 0:
        print(f"#{_} Alice")
    else:
        print(f"#{_} Bob")
