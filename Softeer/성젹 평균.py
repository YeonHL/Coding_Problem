n, k = map(int, input().split())
_grade = list(map(int, input().split()))

for _ in range(k):
    a, b = map(int, input().split())
    print(format(sum(_grade[a-1:b]) / (b+1-a), ".2f"))
