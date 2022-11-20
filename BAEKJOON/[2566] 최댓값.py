A = [list(map(int, input().split())) for _ in range(9)]
_max = 0
ans = (0, 0)

for i in range(9):
    for j in range(9):
        if A[i][j] >= _max:
            _max = A[i][j]
            ans = (i+1, j+1)

print(_max)
print(ans[0], ans[1])
