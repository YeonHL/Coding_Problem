""" import sys
rl = sys.stdin.readline

n = int(rl())
l = list(map(int, rl().split()))

_number = list(set(l))
_number.sort()
_table = {}

for i in range(len(_number)):
    _table[_number[i]] = i

for i in range(n):
    print(_table[l[i]], end=' ') """

import sys
rl = sys.stdin.readline

n = int(rl())
l = list(map(int, rl().split()))

arr = sorted(set(l))
_table = {n: i for i, n in enumerate(arr)}

print(" ".join([str(_table[num]) for num in l]))

# 입력
# 5
# 2 4 -10 4 -9

# 출력
# 2 3 0 3 1

# 대소 관계만 필요하다면 모든 수를 0 이상 N 미만의 수로 바꿀 수 있다. 정렬, 양수 조건 활용
# 모든 수에 최소만큼 빼면 가능
# 개수와 범위가 매우 크므로 반복문은 최소로

# 1. set로 만들고 list로 다시 변환하여 숫자의 종류를 구한다.
# 2. 앞에서부터 접근하여 그 값을 키로, 인덱스를 값으로 저장한다.
# 3. 테이블을 참고하여 리스트 값을 키로 입력하여 반환을 받는다.
