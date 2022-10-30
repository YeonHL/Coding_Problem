_sum = 0
for _ in range(5):
    a = int(input())
    if a < 40:
        _sum += 40
    else:
        _sum += a

print(_sum // 5)
