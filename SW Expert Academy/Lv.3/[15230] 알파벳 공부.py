t = int(input())

for _ in range(1, t+1):
    s = input()
    i = 0
    cnt = 0
    for c in s:
        if ord(c) == 97+i:
            cnt += 1
            i += 1
        else:
            break
    print(f"#{_}", cnt)
