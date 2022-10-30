import sys
rl = sys.stdin.readline


n, m = map(int, rl().split())
l = list(map(int, rl().split()))

save = 0

for a in range(0, len(l)-2):
    for b in range(a+1, len(l)-1):
        for c in range(b+1, len(l)):
            sum = l[a] + l[b] + l[c]
            if sum <= m and save <= sum:
                save = sum

print(save)

"""
    1. 카드의 수와 목표 값을 입력 받는다.
    map(int, Count & Target)
    2. 카드의 각 숫자를 입력받는다.
    list = map(int, Card)
    3. 카드 3장의 합의 모든 경우의 수를 구한다.
    for a in range(0,len(list)-2)
        for b in range(a+1,len(list)-1)
            for c in range(b+1,len(list))
                sum = list[a] + list[b] + list[c]
                if sum < Target:
                    저장된 합과 비교하여 큰쪽을 저장


"""
