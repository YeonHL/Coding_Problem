import sys

n = int(sys.stdin.readline().rstrip())

if n % 5 == 1:
    ans = (n-6) // 5 + 2
elif n % 5 == 2:
    if n < 12:
        ans = -1
    else:
        ans = (n-12) // 5 + 4
elif n % 5 == 3:
    ans = (n-3) // 5 + 1
elif n % 5 == 4:
    if n < 9:
        ans = -1
    else:
        ans = (n-9) // 5 + 3
else:
    ans = n // 5

print(ans)

# 주어진 숫자의 끝자리에 따라 3의 필요 개수가 달라진다.

# 1 or 6: 2개
# 2 or 7: 4개
# 3 or 8: 1개
# 4 or 9: 3개
