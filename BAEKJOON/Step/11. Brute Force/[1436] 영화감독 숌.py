# (0~5) '666' -> '666' + (0~9) -> (7~9)'666'
# 이후 맨앞에 숫자를 1부터 크기 순서로 더하고 다시 반복
# cur에 현재 숫자 표시, count에 몇번째 숫자인지 표시
# 문자열로 저장, 666의 앞에 오는 숫자를 저장하는 변수 하나 (_front),
# 666(0~9) = 10^1 = 10^len(str(_front))
# 666(00~99) 10^2
# 666

import sys
rl = sys.stdin.readline

N = int(rl())
movie = 666

while N:
    if "666" in str(movie):
        N -= 1
    movie += 1

print(movie - 1)
