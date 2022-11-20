# 넓이를 구할 경우 가능하다면 작은 단위로 쪼개는 것이 좋다.

paper = [[0]*100 for _ in range(100)]

for _ in range(int(input())):
    y, x = map(int, input().split())
    for i in range(y, y+10):
        paper[i][x:x+10] = [1]*10

cnt = 0
for p in paper:
    cnt += p.count(1)

print(cnt)
