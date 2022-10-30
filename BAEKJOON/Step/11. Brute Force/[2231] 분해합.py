import sys
rl = sys.stdin.readline

n = int(rl())

r = 0

for i in range(max(0, n-54), n):
    if sum(map(int, list(str(i))))+i == n:
        r = i
        break

print(r)


# 1,000,000 이하이므로 각 자릿수의 합은 최대가 54이다.  n-54 혹은 0부터 n까지의 수 중 생성자가 있는지 확인
