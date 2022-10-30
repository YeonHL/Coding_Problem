import sys
rl = sys.stdin.readline

result = []


def cut_paper(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                cut_paper(x, y, N//2)
                cut_paper(x, y+N//2, N//2)
                cut_paper(x+N//2, y, N//2)
                cut_paper(x+N//2, y+N//2, N//2)
                return 0
    if color == '0':
        result.append(0)
    else:
        result.append(1)


n = int(rl())
paper = [list(rl().split()) for _ in range(n)]

cut_paper(0, 0, n)
print(result.count(0))
print(result.count(1))

# 재귀 이용, 4등분, N/2이 모두 같은 값을 갖는지 확인
# 입력으로 총 길이와 좌표 정보를 제공한다.
# n: 종이의 길이, p: 종이의 색 상태, c: 구하려는 종이의 색

# 1. 변수를 만들고 종이의 수만큼 더하기
# 2. 각 계산마다 종이의 수를 계산해서 반환하기
