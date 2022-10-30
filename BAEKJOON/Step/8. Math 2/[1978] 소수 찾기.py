import sys
rl = sys.stdin.readline

n = int(rl())
a = list(map(int, rl().split()))

i = 2
count = 0
list = [2]

while (i <= max(a)):
    for z in list:
        if i % z == 0:
            break
        elif z == list[-1]:
            list.append(i)
            break
    i += 1


for y in a:
    if y in list:
        count += 1

print(count)

# 입력한 수와 그 크기가 클 때를 대비하여 소수를 저장하는 방식으로 작성했다.
